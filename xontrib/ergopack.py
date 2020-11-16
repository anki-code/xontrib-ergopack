from xonsh import xontribs

_xontribs = [
  'argcomplete',
  'back2dir',
  'output_search',
  'pipeliner',
  'sh',
  'whole_word_jumping',  # xonsh built in
]

_xontribs = __xonsh__.env.get('XONTRIB_ERGOPACK_XONTRIBS', _xontribs)

xontribs.xontribs_load(_xontribs)
