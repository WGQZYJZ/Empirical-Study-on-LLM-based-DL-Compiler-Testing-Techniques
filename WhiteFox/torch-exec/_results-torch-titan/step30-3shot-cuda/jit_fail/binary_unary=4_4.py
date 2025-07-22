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
        self.linear = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = (v1 + other)
        v3 = (v2 + additional_tensor)
        return v3




func = Model().to('cuda')



other = torch.randn(1, 1, 64, 64)



additional_tensor = torch.randn(1, 1, 64, 64)



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [other, additional_tensor, x1]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 4 were given

jit:
forward() takes 2 positional arguments but 4 were given
'''