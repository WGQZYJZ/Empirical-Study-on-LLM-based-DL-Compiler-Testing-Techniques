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
        self.conv = torch.nn.Conv2d(3, 2, 2, stride=1, padding=2)

    def forward(self, x1):
        v1 = self.conv(x1)
        vt = v1.sigmoid()
        v3 = torch._C._nn.ctc_loss(v1, vt.cpu()) * v1
        return v3



func = Model().to('cpu')


v1 = torch.randn(1, 128, 8)
v1 = torch.randn(1, 128, 8)
v2 = v1.sigmoid()

test_inputs = [v1, v2]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 3 were given

jit:
forward() takes 2 positional arguments but 3 were given
'''