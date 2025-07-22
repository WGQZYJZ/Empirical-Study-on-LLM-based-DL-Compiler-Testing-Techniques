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

    def forward(self, x1, x2):
        v1 = torch.cat((x1, x2), dim=1)
        v2 = v1[:, 0:9223372036854775807]
        v3 = v2[:, 0:10]
        v4 = torch.cat((v1, v3), dim=1)
        return v4



func = Model().to('cuda')



x1 = torch.randn(1, 20, 416, 416)



x2 = torch.randn(1, 20, 416, 416)



x3 = torch.randn(1, 20, 416, 416)



x4 = torch.randn(1, 20, 416, 416)



x5 = torch.randn(1, 20, 416, 416)



x6 = torch.randn(1, 20, 416, 416)



x7 = torch.randn(1, 20, 416, 416)



x8 = torch.randn(1, 20, 416, 416)



x9 = torch.randn(1, 20, 416, 416)



x10 = torch.randn(1, 20, 416, 416)



x11 = torch.randn(1, 20, 416, 416)


test_inputs = [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11]

# JIT_FAIL
'''
direct:
forward() takes 3 positional arguments but 12 were given

jit:
forward() takes 3 positional arguments but 12 were given
'''