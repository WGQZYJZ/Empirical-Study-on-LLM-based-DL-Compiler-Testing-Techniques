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
        self.linear = torch.nn.Linear(100, 100)

    def forward(self, x1, x2):
        v1 = self.linear(x1)
        v2 = (v1 + x2)
        return v2



func = Model().to('cuda')



x1 = torch.randn(1, 100)



x2 = torch.randn(1, 100)



x3 = torch.randn(1, 100)


test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
forward() takes 3 positional arguments but 4 were given

jit:
forward() takes 3 positional arguments but 4 were given
'''