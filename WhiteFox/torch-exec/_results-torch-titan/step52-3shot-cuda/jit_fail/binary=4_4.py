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
        self.linear = torch.nn.Linear(3, 6)

    def forward(self, x2):
        v2 = self.linear(x2)
        v3 = (v2 + other)
        return v3



func = Model().to('cuda')



x2 = torch.randn(1, 3)



other = torch.randn(1, 6)


test_inputs = [x2, other]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 3 were given

jit:
forward() takes 2 positional arguments but 3 were given
'''