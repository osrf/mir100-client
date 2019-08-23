import enum
import sys
import xml.sax
from xml.sax import ContentHandler
import yaml


def print_path(path):
  print('\t' * 10, path['op'], path['path'])
  print('Description:', path['desc'])
  print('Parameters:')
  for param in path['params']:
    print('\ttype:', param['type'])
    print('\tname:', param['name'])
    print('\tdesc:', param['desc'])
    print('\tschema:', param['schema'])
    print('\t---')
  print('Responses:')
  for response in path['responses']:
    print('\tcode:', response['code'])
    print('\tdesc:', response['desc'])
    print('\tschema:', response['schema'])
    print('\t---')
  print()

class PathsHandler(ContentHandler):
  class State(enum.Enum):
    DOC_START = enum.auto()
    OP = enum.auto()
    PATH = enum.auto()
    DESC_START = enum.auto()
    DESC = enum.auto()
    PARAM_TYPE_HEADER = enum.auto()
    PARAM_NAME_HEADER = enum.auto()
    PARAM_DESC_HEADER = enum.auto()
    PARAM_SCHEMA_HEADER = enum.auto()
    PARAMS = enum.auto()
    RESP_CODE_HEADER = enum.auto()
    RESP_DESC_HEADER = enum.auto()
    RESP_SCHEMA_HEADER = enum.auto()
    RESPONSES = enum.auto()
    TAGS = enum.auto()

  class Word():
    def __init__(self, xmin, ymin, content):
      self.x = xmin
      self.y = ymin
      self.content = content

  ParamTypes = ['Header', 'Path', 'Body']
  FOOTER_MARGIN = 800
  PARAM_MARGIN = 20
  RESP_MARGIN = 20

  def __init__(self):
    self.skip = True
    self.skip_word = 0
    self.state = PathsHandler.State.DOC_START
    self.paths = []
    self.path = {}
    self.attrs = None

  def startElement(self, name, attrs):
    if name == 'word':
      self.attrs = attrs
      self.skip = False

  def endElement(self, name):
    if name == 'word':
      self.skip = True

  def characters(self, content):
    if self.skip:
      return

    if self.skip_word:
      self.skip_word -= 1
      return

    if float(self.attrs['yMin']) > PathsHandler.FOOTER_MARGIN:
      return

    if self.state == PathsHandler.State.OP:
      self.path = {}
      self.path['op'] = content
      self.state = PathsHandler.State.PATH
    elif self.state == PathsHandler.State.PATH:
      self.path['path'] = content
      self.state = PathsHandler.State.DESC_START
    elif self.state == PathsHandler.State.DESC_START:
      if content == 'Description':
        self.path['desc'] = ''
        self.state = PathsHandler.State.DESC
    elif self.state == PathsHandler.State.DESC:
      if self.attrs['xMin'] == '48.240000' and content == 'Parameters':
        self.path['desc'] = self.path['desc'].rstrip()
        self.state = PathsHandler.State.PARAM_TYPE_HEADER
      else:
        self.path['desc'] += content + ' '
    elif self.state == PathsHandler.State.PARAM_TYPE_HEADER:
      self.param_type_xmin = float(self.attrs['xMin'])
      self.state = PathsHandler.State.PARAM_NAME_HEADER
    elif self.state == PathsHandler.State.PARAM_NAME_HEADER:
      self.param_name_xmin = float(self.attrs['xMin'])
      self.state = PathsHandler.State.PARAM_DESC_HEADER
    elif self.state == PathsHandler.State.PARAM_DESC_HEADER:
      self.param_desc_xmin = float(self.attrs['xMin'])
      self.state = PathsHandler.State.PARAM_SCHEMA_HEADER
    elif self.state == PathsHandler.State.PARAM_SCHEMA_HEADER:
      self.param_schema_xmin = float(self.attrs['xMin'])
      self.path['params'] = []
      self.words = []
      self.state = PathsHandler.State.PARAMS
    elif self.state == PathsHandler.State.PARAMS:
      if self.attrs['xMin'] == '48.240000' and content == 'Responses':
        self.words.sort(key=lambda x: (x.y, x.x))
        param = {}
        param['type'] = ''
        param['name'] = ''
        param['desc'] = ''
        param['schema'] = ''
        last_y = self.words[0].y
        for i in range(len(self.words)):
          w = self.words[i]
          if w.y - last_y > PathsHandler.PARAM_MARGIN:
            param['desc'] = param['desc'].rstrip()
            self.path['params'].append(param)
            param = {}
            param['type'] = ''
            param['name'] = ''
            param['desc'] = ''
            param['schema'] = ''

          if w.x >= self.param_type_xmin and w.x < self.param_name_xmin:
            param['type'] += w.content
          elif w.x >= self.param_name_xmin and w.x < self.param_desc_xmin:
            if w.content == 'required':
              param['required'] = True
            else:
              param['name'] += w.content
          elif w.x >= self.param_desc_xmin and w.x < self.param_schema_xmin:
            param['desc'] += w.content + ' '
          else:
            param['schema'] += w.content
          last_y = w.y

        param['desc'] = param['desc'].rstrip()
        self.path['params'].append(param)
        self.state = PathsHandler.State.RESP_CODE_HEADER
      else:
        xmin = float(self.attrs['xMin'])
        ymin = float(self.attrs['yMin'])
        self.words.append(PathsHandler.Word(xmin, ymin, content))
    elif self.state == PathsHandler.State.RESP_CODE_HEADER:
      self.resp_code_xmin = float(self.attrs['xMin'])
      self.skip_word = 1
      self.state = PathsHandler.State.RESP_DESC_HEADER
    elif self.state == PathsHandler.State.RESP_DESC_HEADER:
      self.resp_desc_xmin = float(self.attrs['xMin'])
      self.state = PathsHandler.State.RESP_SCHEMA_HEADER
    elif self.state == PathsHandler.State.RESP_SCHEMA_HEADER:
      self.resp_schema_xmin = float(self.attrs['xMin'])
      self.words = []
      self.path['responses'] = []
      self.state = PathsHandler.State.RESPONSES
    elif self.state == PathsHandler.State.RESPONSES:
      if self.attrs['xMin'] == '48.240000' and content == 'Tags':
        self.words.sort(key=lambda x: (x.y, x.x))
        resp = {}
        resp['code'] = ''
        resp['desc'] = ''
        resp['schema'] = ''
        last_y = self.words[0].y
        for i in range(len(self.words)):
          w = self.words[i]
          if w.y - last_y > PathsHandler.PARAM_MARGIN:
            resp['desc'] = resp['desc'].rstrip()
            self.path['responses'].append(resp)
            resp = {}
            resp['code'] = ''
            resp['desc'] = ''
            resp['schema'] = ''

          if w.x >= self.resp_code_xmin and w.x < self.resp_desc_xmin:
            resp['code'] += w.content
          elif w.x >= self.resp_desc_xmin and w.x < self.resp_schema_xmin:
            resp['desc'] += w.content + ' '
          else:
            resp['schema'] += w.content
          last_y = w.y

        resp['desc'] = resp['desc'].rstrip()
        self.path['responses'].append(resp)
        self.paths.append(self.path)
        self.state = PathsHandler.State.TAGS
      else:
        xmin = float(self.attrs['xMin'])
        ymin = float(self.attrs['yMin'])
        self.words.append(PathsHandler.Word(xmin, ymin, content))
    elif self.state == PathsHandler.State.TAGS:
      if self.attrs['xMin'] == '48.240000':
        self.state = PathsHandler.State.OP
        self.characters(content)
    elif self.state == PathsHandler.State.DOC_START:
      self.state = PathsHandler.State.OP
      if content != 'Paths':
        self.characters(content)

def print_definition(definition):
  print(definition['name'])
  print('=' * 3)
  print('Properties:')
  for prop in definition['properties']:
    print('\tname:', prop['name'])
    if len(prop['desc']):
      print('\tdesc:', prop['desc'])
    print('\tschema:', prop['schema'])
    print()
  print()

class DefinitionsHandler(ContentHandler):
  class State(enum.Enum):
    DOC_START = enum.auto()
    DEFINITION_START = enum.auto()
    PROP_NAME_HEADER = enum.auto()
    PROP_DESC_HEADER = enum.auto()
    PROP_SCHEMA_HEADER = enum.auto()
    DEFINITION = enum.auto()

  class Word():
    def __init__(self, xmin, ymin, content):
      self.x = xmin
      self.y = ymin
      self.content = content

  FOOTER_MARGIN = 800
  CONTINUATION_MARGIN = 42
  PROP_MARGIN = 20

  def __init__(self):
    self.skip = True
    self.skip_word = 0
    self.state = DefinitionsHandler.State.DOC_START
    self.attrs = None
    self.definitions = []
    self.prop = None

  def startElement(self, name, attrs):
    if name == 'word':
      self.attrs = attrs
      self.skip = False

  def endElement(self, name):
    if name == 'word':
      self.skip = True

  def endDocument(self):
    if self.prop:
      self.prop['desc'] = self.prop['desc'].rstrip()
      self.definition['properties'].append(self.prop)
      self.definitions.append(self.definition)

  def characters(self, content):
    if self.skip:
      return

    if self.skip_word:
      self.skip_word -= 1
      return

    if float(self.attrs['yMin']) > DefinitionsHandler.FOOTER_MARGIN:
      return

    if self.state == DefinitionsHandler.State.DEFINITION_START:
      self.definition = {}
      self.definition['name'] = content
      self.properties = {}
      self.state = DefinitionsHandler.State.PROP_NAME_HEADER
    elif self.state == DefinitionsHandler.State.PROP_NAME_HEADER:
      if content == 'Type':
        self.definition['properties'] = []
        self.definitions.append(self.definition)
        self.skip_word = 2
        self.state = DefinitionsHandler.State.DEFINITION_START
      else:
        self.def_name_xmin = float(self.attrs['xMin'])
        self.state = DefinitionsHandler.State.PROP_DESC_HEADER
    elif self.state == DefinitionsHandler.State.PROP_DESC_HEADER:
      if content == 'Schema':
        self.def_has_desc = False
        self.def_desc_xmin = float(self.attrs['xMin'])
        self.state = DefinitionsHandler.State.PROP_SCHEMA_HEADER
        self.characters(content)
      else:
        self.def_has_desc = True
        self.def_desc_xmin = float(self.attrs['xMin'])
        self.state = DefinitionsHandler.State.PROP_SCHEMA_HEADER
    elif self.state == DefinitionsHandler.State.PROP_SCHEMA_HEADER:
      self.def_schema_xmin = float(self.attrs['xMin'])
      self.words = []
      self.definition['properties'] = []
      self.state = DefinitionsHandler.State.DEFINITION
    elif self.state == DefinitionsHandler.State.DEFINITION:
      if self.attrs['xMin'] == '48.240000':
        self.prop = {}
        self.prop['name'] = ''
        self.prop['desc'] = ''
        self.prop['schema'] = ''
        last_y = self.words[0].y
        for i in range(len(self.words)):
          w = self.words[i]

          if w.y < DefinitionsHandler.CONTINUATION_MARGIN:
            if w.content == 'Name':
              self.prop['desc'] = self.prop['desc'].rstrip()
              self.definition['properties'].append(self.prop)
              self.prop = {}
              self.prop['name'] = ''
              self.prop['desc'] = ''
              self.prop['schema'] = ''
            continue

          if w.y - last_y > DefinitionsHandler.PROP_MARGIN:
            self.prop['desc'] = self.prop['desc'].rstrip()
            self.definition['properties'].append(self.prop)
            self.prop = {}
            self.prop['name'] = ''
            self.prop['desc'] = ''
            self.prop['schema'] = ''

          self.process_prop_word(w, self.prop)
          last_y = w.y

        self.prop['desc'] = self.prop['desc'].rstrip()
        self.definition['properties'].append(self.prop)
        self.definitions.append(self.definition)
        self.state = DefinitionsHandler.State.DEFINITION_START
        self.characters(content)
      else:
        xmin = float(self.attrs['xMin'])
        ymin = float(self.attrs['yMin'])
        self.words.append(DefinitionsHandler.Word(xmin, ymin, content))
    elif self.state == DefinitionsHandler.State.DOC_START:
      self.state = DefinitionsHandler.State.DEFINITION_START

  def process_prop_word(self, w, prop):
    if w.x >= self.def_name_xmin and w.x < self.def_desc_xmin:
      if w.content == 'optional':
        prop['required'] = False
      elif w.content == 'required':
        prop['required'] = True
      else:
        prop['name'] += w.content
    elif self.def_has_desc and w.x >= self.def_desc_xmin and w.x < self.def_schema_xmin:
      prop['desc'] += w.content + ' '
    else:
      prop['schema'] += w.content

paths_handler = PathsHandler()
xml.sax.parse('mir_mir100_rest_api_270-paths.xml', paths_handler)

def_handler = DefinitionsHandler()
xml.sax.parse('mir_mir100_rest_api_270-schemas.xml', def_handler)

def to_oapi_schema(schema):
  if schema.startswith('enum'):
    return {'type': 'string'}
  elif schema.startswith('string('):
    start = schema.index('(') + 1
    end = schema.index(')')
    return {'type': 'string', 'format': f'{schema[start:end]}'}
  elif schema == 'string' or schema == 'object' or schema == 'boolean':
    return {'type': schema}
  elif schema == 'integer':
    return {'type': 'integer', 'format': 'int64'}
  elif schema == 'integer(float)':
    return {'type': 'integer', 'format': 'int64'}
  elif schema == 'integer(int32)':
    return {'type': 'integer', 'format': 'int32'}
  elif schema == 'number(float)':
    return {'type': 'number', 'format': 'float'}
  elif schema == 'NoContent':
    return {'type': 'null'}
  elif schema.endswith('array'):
    array_oapi = {}
    array_oapi['type'] = 'array'
    item_schema = schema[1:schema.index('>')]
    array_oapi['items'] = to_oapi_schema(item_schema)
    return array_oapi
  else:
    return {'$ref': f'#/components/schemas/{schema}'}

def is_no_content(schema):
  if schema.get('type') == 'null':
    return True
  return False

root_oapi = {}
root_oapi['openapi'] = '3.0.1'
root_oapi['info'] = {}
info_oapi = root_oapi['info']
info_oapi['title'] = 'MIR100 Rest Interface'
info_oapi['description'] = 'Automatically converted from v270 pdf'
info_oapi['version'] = '2.7.0'
root_oapi['paths'] = {}
paths_oapi = root_oapi['paths']

for path in paths_handler.paths:
  op_oapi = {}
  op_oapi['summary'] = path['desc']
  params_oapi = []
  body_param = None
  for param in path['params']:
    # authorization is described in security schemes
    if param['name'] == 'Authorization':
      continue

    param_oapi = {}
    if param['type'] != 'Body':
      param_oapi['in'] = param['type'].lower()
    else:
      body_param = param
      continue
    param_oapi['name'] = param['name']
    param_oapi['description'] = param['desc']
    if param.get('required'):
      param_oapi['required'] = True
    param_oapi['schema'] = to_oapi_schema(param['schema'])

    # some post processing to make 'Accept-Language' default to 'en-US'
    if param_oapi['name'] == 'Accept-Language':
      del param_oapi['required']
      param_oapi['schema']['default'] = 'en-US'

    params_oapi.append(param_oapi)
  op_oapi['parameters'] = params_oapi

  if body_param:
    body_oapi = {}
    body_oapi['description'] = body_param['desc']
    if body_param.get('required'):
      body_oapi['required'] = True
    content_oapi = {}
    media_oapi = {}
    media_oapi['schema'] = to_oapi_schema(body_param['schema'])
    content_oapi['application/json'] = media_oapi
    body_oapi['content'] = content_oapi
    op_oapi['requestBody'] = body_oapi

  resps_oapi = {}
  for resp in path['responses']:
    resp_oapi = {}
    resp_oapi['description'] = resp['desc']
    content_oapi = {}
    media_oapi = {}
    oapi_schema = to_oapi_schema(resp['schema'])
    if not is_no_content(oapi_schema):
      media_oapi['schema'] = to_oapi_schema(resp['schema'])
      content_oapi['application/json'] = media_oapi
      resp_oapi['content'] = content_oapi
    resps_oapi[resp['code']] = resp_oapi

  op_oapi['responses'] = resps_oapi

  path_oapi = paths_oapi.setdefault(path['path'], {})
  path_oapi[path['op'].lower()] = op_oapi

schemas_oapi = {}
for definition in def_handler.definitions:
  schema_oapi = {}
  schema_oapi['type'] = 'object'
  props_oapi = {}
  required = []
  for prop in definition['properties']:
    prop_oapi = {}
    # parameters is wrongly set as string somethings in the pdf
    if prop['name'] == 'parameters':
      prop_oapi['type'] = 'array'
      prop_oapi['items'] = {'type': 'object'}
    else:
      prop_oapi.update(to_oapi_schema(prop['schema']))
    if len(prop['desc']):
      prop_oapi['description'] = prop['desc']
    props_oapi[prop['name']] = prop_oapi
    if prop.get('required'):
      required.append(prop['name'])
  if len(required):
    schema_oapi['required'] = required
  schema_oapi['properties'] = props_oapi
  schemas_oapi[definition['name']] = schema_oapi

root_oapi['components'] = {}
root_oapi['components']['schemas'] = schemas_oapi

# security scheme
root_oapi['components']['securitySchemes'] = {}
security_oapi = root_oapi['components']['securitySchemes']['mir'] = {}
security_oapi['type'] = 'http'
security_oapi['scheme'] = 'Basic'
security_oapi['description'] = 'username followed by a colon and the password sha-256 encoded. Ex: BASE64(\\<username\\>:SHA-256(\\<password\\>))'
root_oapi['security'] = [{'mir': []}]

print(yaml.dump(root_oapi))
