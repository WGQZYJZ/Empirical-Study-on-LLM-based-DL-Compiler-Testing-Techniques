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
        self.conv = torch.nn.Conv2d(3, 3, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = (v1 + 3)
        v3 = torch.clamp(v2, 0, 6)
        v4 = (v1 * v3)
        v5 = (v4 / 6)
        return v5




func = Model().to('cuda')



x1 = torch.randn(2, 3, 64, 64)



x2 = torch.randn(2, 3, 1, 1)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 3 were given

jit:
forward() takes 2 positional arguments but 3 were given
'''