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
        self.test = 0

    def forward(self, x):
        x = (x.view(10, 10).permute(1, 0) if (x.shape != (10, 10)) else x)
        out = torch.cat([x, x, x], dim=(- 1))
        return out




func = Model().to('cuda')



x = torch.rand((1, 1))



y = torch.rand((1, 1))



z = torch.rand((1, 1))


test_inputs = [x, y, z]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 4 were given

jit:
forward() takes 2 positional arguments but 4 were given
'''