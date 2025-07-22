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

    def __init__(self, input1):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.input1 = input1

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = (v1 + self.input1)
        return v2




input1 = torch.randn(1, 3, 64, 64)

func = Model(input1).to('cuda')



input1 = torch.randn(1, 3, 64, 64)



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [input1, x1]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 3 were given

jit:
forward() takes 2 positional arguments but 3 were given
'''