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



class Model(torch.nn.Module):

    def __init__(self):
        super().__init__()

    def forward(self, x1, other=0):
        (v1, o1) = x1.chunk(2, dim=1)
        if (other > 0):
            (v2, o2) = x1.chunk(2, dim=2)
        v3 = (((v1 * float(other)) + o1) + o2)
        return v3




func = Model().to('cuda')



x1 = torch.randn(1, 4, 4, 4)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
local variable 'o2' referenced before assignment

jit:
local variable 'o2' referenced before assignment
'''