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

    def __init__(self, negative_slope=0.3):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 3, stride=1, padding=1)
        self.negative_slope = negative_slope

    def forward(self, x):
        v1 = self.conv(x)
        v2 = torch.gt(v1, 0)
        v3 = v2.type(dtype=v1.dtype)
        v4 = torch.mul(v1, self.negative_slope)
        v5 = torch.where(v2, v1, v4)
        return v5



func = Model().to('cuda')



x = torch.randn(1, 3, 64, 64)


test_inputs = [x]

# JIT_STATUS
'''
direct:


jit:
Tensor.type() unhandled kwargs

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''