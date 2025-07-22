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
        self.conv = torch.nn.Conv2d(1, 1, 1, stride=1, padding=0)
        self.bn = torch.nn.BatchNorm2d(1, eps=1, track_running_stats=True)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.flatten(v1.T, 1)
        v3 = self.bn(v2)
        return v3



func = Model().to('cpu')


x1 = torch.randn(2, 1, 192, 182)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
expected 4D input (got 2D input)

jit:
expected 4D input (got 2D input)
'''