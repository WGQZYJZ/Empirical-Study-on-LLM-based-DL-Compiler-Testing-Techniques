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

    def forward(self, x4):
        v1 = torch.cat(x4, dim=1)
        v2 = v1[:, (- 1)]
        return v2



func = Model().to('cuda')



x4_1 = torch.randn(1, 7680)



x4_2 = torch.randn(1, 1600000)



x4_3 = torch.randn(1, 10000000)


test_inputs = [x4_1, x4_2, x4_3]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 4 were given

jit:
forward() takes 2 positional arguments but 4 were given
'''