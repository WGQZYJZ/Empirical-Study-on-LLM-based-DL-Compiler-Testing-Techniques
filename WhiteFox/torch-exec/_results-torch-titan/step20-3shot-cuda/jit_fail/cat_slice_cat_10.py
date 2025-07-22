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

    def __init__(self, size):
        super().__init__()

    def forward(self, x):
        v2 = x[0:4294967295, :, :, :]
        v3 = v2[:, 0:size, :, :]
        v4 = torch.cat([x, v3], dim=1)
        return v4



size = 1

func = Model(size).to('cuda')



x1 = torch.randn(1, 13, 64, 64)



x2 = torch.randn(1, 17, 64, 64)



x3 = torch.randn(1, 19, 64, 64)


test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 4 were given

jit:
forward() takes 2 positional arguments but 4 were given
'''