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

    def forward(self, x1):
        v1 = x1
        v2 = v1
        v3 = v2[:, :, 0:64]
        v4 = torch.cat([v1, v3], dim=1)
        v5 = torch.cat([v4, v4], dim=0)
        return v5



func = Model().to('cuda')



x1 = torch.randn(5, 3, 128, 128)



x2 = torch.randn(1, 10, 256, 256)



x3 = torch.randn(11, 5, 64, 64)



x4 = torch.randn(3, 1, 512, 512)



x5 = torch.randn(20, 2, 64, 64)



x6 = torch.randn(7, 5, 256, 256)


test_inputs = [x1, x2, x3, x4, x5, x6]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 7 were given

jit:
forward() takes 2 positional arguments but 7 were given
'''