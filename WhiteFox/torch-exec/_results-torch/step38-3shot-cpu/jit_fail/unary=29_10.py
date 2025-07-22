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

    def __init__(self, min_value=-0.00655, max_value=0.0139503):
        super().__init__()
        self.sigmoid = torch.sigmoid
        self.conv_transpose = torch.nn.ConvTranspose2d(5, 3, 1, stride=1, padding=0, dilation=1)
        self.max_pool = torch.nn.MaxPool2d(kernel_size=2, stride=1, padding=0, dilation=1, ceil_mode=True)
        self.adaptive_avg_pool2d = torch.nn.AdaptiveAvgPool2d((1, 1))
        self.add = torch.add
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x3):
        v1 = self.conv_transpose(x3)
        v2 = torch.clamp_min(v1, self.min_value)
        v3 = torch.clamp_max(v2, self.max_value)
        v4 = torch.sigmoid(v3)
        z2 = self.max_pool(v4)
        r2 = self.adaptive_avg_pool2d(z2)
        v5 = r2.sum(axis=[2, 3])
        z3 = self.add(r2, r2)
        r3 = z3.sum(axis=[2, 3])
        z4 = self.leaky_relu(r3)
        r4 = z4.sum(axis=[2, 3])
        z5 = self.adaptive_avg_pool2d(z4)
        r5 = z5.sum(axis=[2, 3])
        v6 = self.sigmoid(r5)
        return v6



func = Model().to('cpu')


x3 = torch.randn(1, 5, 112, 112)

test_inputs = [x3]

# JIT_FAIL
'''
direct:
'Model' object has no attribute 'leaky_relu'

jit:
'Model' object has no attribute 'leaky_relu'
'''