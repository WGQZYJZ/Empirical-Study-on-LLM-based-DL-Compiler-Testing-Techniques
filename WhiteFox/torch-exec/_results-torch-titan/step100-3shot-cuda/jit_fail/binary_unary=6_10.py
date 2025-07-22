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
        self.linear = torch.nn.Linear(1024, 20000)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = (- 2.5e-07)
        v3 = (v1 - v2)
        v4 = torch.nn.functional.relu(v3)
        return v4



func = Model().to('cuda')



x1 = torch.randn(1, 1024)



x2 = torch.randn(1, 20000)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 3 were given

jit:
forward() takes 2 positional arguments but 3 were given
'''