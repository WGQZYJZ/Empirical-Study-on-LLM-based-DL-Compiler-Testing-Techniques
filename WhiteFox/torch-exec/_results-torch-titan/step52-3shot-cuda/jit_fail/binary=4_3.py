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
        self.linear = torch.nn.Linear(50, 50, bias=True)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = (v1 + other)
        return v2



func = Model().to('cuda')



x1 = torch.randn(100, 50)



other = torch.randn(100, 50)


test_inputs = [x1, other]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 3 were given

jit:
forward() takes 2 positional arguments but 3 were given
'''