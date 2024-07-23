__version__ = '0.0.1'

from ._fortran import fortran as __fortran
printing = __fortran.printing

__all__ = ['fortran', 'printing']
