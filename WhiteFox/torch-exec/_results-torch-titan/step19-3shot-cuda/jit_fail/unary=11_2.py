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
        self.conv_transpose = torch.nn.ConvTranspose2d(9, 32, 2, stride=2, padding=1)

    def forward(self, x1, x2, x3, x4):
        v0 = (x0 + x1)
        v1 = torch.cat((x2, x3, x4), 1)
        v2 = self.conv_transpose(v1)
        v3 = (v2 + 3)
        v4 = torch.clamp_min(v3, 0)
        v5 = torch.clamp_max(v4, 6)
        v6 = (v5 / 6)
        return v6




func = Model().to('cuda')



x0 = torch.randn(1, 3, 28, 28)



x1 = torch.randn(1, 3, 28, 28)



x2 = torch.randn(1, 3, 28, 28)



x3 = torch.randn(1, 3, 28, 28)



x4 = torch.randn(1, 3, 28, 28)


test_inputs = [x0, x1, x2, x3, x4]

# JIT_FAIL
'''
direct:
forward() takes 5 positional arguments but 6 were given

jit:
forward() takes 5 positional arguments but 6 were given
'''