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
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v3 = torch.add(x1, v1)
        v1 = torch.nn.functional.linear(v3, self.linear.weight, self.linear.bias)
        v2 = v1.permute(0, 2, 1)
        return v2




func = Model().to('cuda')



x1 = torch.randn(6, 2, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
local variable 'v1' referenced before assignment

jit:
local variable 'v1' referenced before assignment
'''