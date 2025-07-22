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
        v1 = torch.cat([x1, x2], dim=1)
        return v1[:, 0:9223372036854775807, 0:6]



func = Model().to('cuda')



size = torch.randint(1, 5, [1])



x1 = torch.randn(3, 7, 5)



x2 = torch.randn(3, 7, 5)


test_inputs = [size, x1, x2]

# JIT_FAIL
'''
direct:
forward() takes 3 positional arguments but 4 were given

jit:
forward() takes 3 positional arguments but 4 were given
'''