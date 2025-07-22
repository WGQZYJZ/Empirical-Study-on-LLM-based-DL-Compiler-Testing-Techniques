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
        self.linear = torch.nn.Linear(3, 6, bias=False)

    def forward(self, x1, x2, inp):
        v1 = self.linear(v2)
        v2 = (v1.t() + x1)
        v3 = torch.mm(v2, x2)
        return v3




func = Model().to('cuda')



x1 = torch.randn(3, 3, requires_grad=True)



x2 = torch.randn(3, 3, requires_grad=True)



inp = torch.randn(3, 3)


test_inputs = [x1, x2, inp]

# JIT_FAIL
'''
direct:
local variable 'v2' referenced before assignment

jit:
local variable 'v2' referenced before assignment
'''