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
        self.linear = torch.nn.Linear(64, 16, bias=False)

    def forward(self, x2):
        v1 = self.linear(x2)
        v2 = (v1 + x2)
        return v2



func = Model().to('cuda')



x2 = torch.randn(1, 64)



x3 = torch.randn(1, 64)


test_inputs = [x2, x3]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 3 were given

jit:
forward() takes 2 positional arguments but 3 were given
'''