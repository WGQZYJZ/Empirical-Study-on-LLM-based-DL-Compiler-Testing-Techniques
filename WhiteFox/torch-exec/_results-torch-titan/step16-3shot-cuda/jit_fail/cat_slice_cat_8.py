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
        v1 = torch.cat([x1, x1], dim=1)
        v2 = v1[:, 0:torch.iinfo(torch.int64).max]
        v3 = v2[:, 0:6]
        v4 = torch.cat([v1, v3], dim=1)
        return v4



func = Model().to('cuda')



x1 = torch.randn(8, 6, 3)



x2 = torch.randn(8, 6, 3)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 3 were given

jit:
forward() takes 2 positional arguments but 3 were given
'''