"""
Python EDA Package
"""

__version__ = "0.12.0"

import pyeda.alphas
import pyeda.arithmetic

from pyeda.binop import (
    apply2,
    OP_ZERO, OP_AND,  OP_GT,   OP_FST, OP_LT,   OP_SND, OP_XOR,  OP_OR,
    OP_NOR,  OP_XNOR, OP_NSND, OP_GTE, OP_NFST, OP_LTE, OP_NAND, OP_ONE
)

from pyeda.boolfunc import (
    num2point, num2upoint, num2term, point2upoint, point2term,
    iter_points, iter_upoints, iter_terms
)

from pyeda.common import clog2, boolify, pcify

from pyeda.bdd import bddvar, expr2bdd, bdd2expr
from pyeda.expr import (
    exprvar, var,
    Nor, Nand, OneHot0, OneHot,
    Not, Or, And, Xor, Xnor, Equal, Implies, ITE
)
from pyeda.vexpr import BitVector, bitvec, uint2vec, int2vec
from pyeda.nfexpr import expr2nfexpr, expr2nfexpr, CNF_And, DNF_Or
from pyeda.table import ttvar, expr2truthtable, truthtable2expr, TruthTable

from pyeda.dimacs import load_cnf, dump_cnf, load_sat, dump_sat
