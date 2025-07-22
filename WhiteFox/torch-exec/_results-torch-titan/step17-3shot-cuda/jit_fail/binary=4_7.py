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
        self.linear = torch.nn.Linear(2, 8)

    def forward(self, x1, x2):
        v1 = self.linear(x1)
        v2 = (v2 + x2)
        return v2



func = Model().to('cuda')



x1 = torch.randn(1, 2)



x2 = torch.randn(1, 8, 4, 4)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
local variable 'v2' referenced before assignment

jit:
local variable 'v2' referenced before assignment
'''