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
        self.conv = torch.nn.Conv2d(2, 3, 1, groups=1, bias=True)
        self.add = torch.nn.quantized.FloatFunctional()

    def forward(self, x1):
        x1 = torch.rand(1, 2, 3, 3)
        x1 = self.conv(x1)
        x1 = self.add.mul(x1, (x1 * 2))
        x1 = self.add.mul(x1, (x1 * 2))
        x1 = self.add.mul(x1, (x1 * 2))
        x1 = self.add.mul(x1, (x1 * 2))
        v2 = x1.to(torch.int64)
        return v2




func = Model().to('cuda')



x1 = torch.randn(1, 2, 3, 3)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cpu and cuda:0! (when checking argument for argument weight in method wrapper_CUDA___slow_conv2d_forward)

jit:
Expected all tensors to be on the same device, but found at least two devices, cpu and cuda:0! (when checking argument for argument weight in method wrapper_CUDA___slow_conv2d_forward)
'''