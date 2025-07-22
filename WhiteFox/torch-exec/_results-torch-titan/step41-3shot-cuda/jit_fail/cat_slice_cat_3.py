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
        v1 = x1.shape[1]
        v2 = (v1 // 2)
        v3 = (v1 - v2)
        t1 = torch.cat([x1, x1], dim=1)
        t2 = t1[:, 0:9223372036854775807]
        t3 = t2[:, 0:v2]
        t4 = torch.cat([t1, t3], dim=1)
        v4 = t4[:, 0:10, 0:10, 0:10]
        v5 = t4[:, v3:(10 + v3), 0:10, 0:10]
        v6 = t4[:, 0:10, v3:(10 + v3), 0:10]
        v7 = t4[:, 0:10, 0:10, v3:(10 + v3)]
        return (((v4 + v5) + v6) + v7)



func = Model().to('cuda')



x1 = torch.randn(1, 10, 10, 10)



x2 = torch.randn(1, 20, 10, 10)



x3 = torch.randn(1, 30, 10, 10)



x4 = torch.randn(1, 40, 10, 10)



x5 = torch.randn(1, 50, 10, 10)



x6 = torch.randn(1, 60, 10, 10)


test_inputs = [x1, x2, x3, x4, x5, x6]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 7 were given

jit:
forward() takes 2 positional arguments but 7 were given
'''