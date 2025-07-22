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
        self.linear = torch.nn.Linear(3, 8, bias=True)

    def forward(self, x1, other=None):
        v1 = self.linear(x1)
        if (other is None):
            v = v1
        v = (v + other)
        return v



func = Model().to('cuda')



x1 = torch.randn(1, 3)



x2 = torch.randn(1, 3)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
local variable 'v' referenced before assignment

jit:
local variable 'v' referenced before assignment
'''