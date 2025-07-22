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

    def __init__(self, other):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.other = other

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = (v1 + self.other)
        return v2



other = 1

func = Model(other).to('cuda')



other_tensor = torch.randn(1, 8, 64, 64, requires_grad=True)



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [other_tensor, x1]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 3 were given

jit:
forward() takes 2 positional arguments but 3 were given
'''