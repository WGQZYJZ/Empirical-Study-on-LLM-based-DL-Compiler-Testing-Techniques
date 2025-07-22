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
        self.conv = torch.nn.Conv2d(3, 1, 3)
        self.bn = torch.nn.BatchNorm1d(1)

    def forward(self, x1):
        s = self.conv(x1)
        t = self.bn(s)
        return t



func = Model().to('cpu')


x1 = torch.randn(1, 3, 6, 6)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
expected 2D or 3D input (got 4D input)

jit:
expected 2D or 3D input (got 4D input)
'''