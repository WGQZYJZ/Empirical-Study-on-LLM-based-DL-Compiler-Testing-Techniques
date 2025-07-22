import os
import torch
import torch.nn.functional as F
import torch.nn as nn
import numpy as np
from torch.autograd import Variable
import math
import torch as th
import torch.linalg as la
from torch.nn import Parameter
import torch.linalg as linalg

class model(torch.nn.Module):

    def __init__(self):
        super().__init__()

    def forward(self, x):
        m = self._module
        t1 = torch.nn.functional.dropout(x, p=0.4)
        return 1



func = model().to('cpu')


x1 = torch.randn(1, 2, 2)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
'model' object has no attribute '_module'

jit:
'model' object has no attribute '_module'
'''