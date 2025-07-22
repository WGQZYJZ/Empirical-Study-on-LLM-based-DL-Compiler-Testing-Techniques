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
        self.avgpool = torch.nn.AvgPool2d(3, stride=1, padding=1)
        self.conv = torch.nn.Conv2d(3, 3, 3, stride=1, padding=1)

    def forward(self, x):
        negative_slope = 1.811989
        v1 = self.avgpool(x)
        v2 = self.conv(x1)
        v3 = (v2 > 0)
        v4 = (v2 * negative_slope)
        v5 = torch.where(v3, v2, v4)
        return v5




func = Model().to('cuda')



x1 = torch.randn(1, 3, 10, 10)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cpu and cuda:0! (when checking argument for argument weight in method wrapper_CUDA___slow_conv2d_forward)

jit:
Expected all tensors to be on the same device, but found at least two devices, cpu and cuda:0! (when checking argument for argument weight in method wrapper_CUDA___slow_conv2d_forward)
'''