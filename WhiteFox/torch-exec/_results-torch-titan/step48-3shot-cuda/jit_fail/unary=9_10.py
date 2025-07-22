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
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = torch.add(self.conv, 3)
        v3 = v1.clamp(min=0, max=6)
        v4 = torch.divide(v3, 6)
        return v4




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
add(): argument 'input' (position 1) must be Tensor, not Conv2d

jit:
add(): argument 'input' (position 1) must be Tensor, not Conv2d
'''