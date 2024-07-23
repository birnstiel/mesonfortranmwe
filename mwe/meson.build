python_sources = ['__init__.py']
py3.install_sources(python_sources, subdir: 'mwe')

fortran_sources = ['fortran.f90']

source = custom_target('fortranmodule.c',
  input: fortran_sources,
  output: ['fortranmodule.c'],
  command: [py3, '-m', 'numpy.f2py', '--lower', '-m', 'fortran', '@INPUT@', '--build-dir', 'mwe']
  )
py3.extension_module('fortran',
  fortran_sources + source,
  incdir_f2py / 'fortranobject.c',
  include_directories: inc_np,
  dependencies: py_dep,
  install: true,
  subdir: 'mwe')
