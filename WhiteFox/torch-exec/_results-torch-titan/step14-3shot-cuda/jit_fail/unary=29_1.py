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

    def __init__(self, min_value=(- 4.2), max_value=(- 2.3), input_channels=3):
        super().__init__()
        t = torch.nn.ConvTranspose2d(input_channels, 8, 1, stride=1, padding=1)
        self.weight = torch.nn.Parameter(t.weight.data.transpose(1, 3))
        self.bias = torch.nn.Parameter(t.bias)
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x1):
        t1 = torch.clamp_min(self.bias, self.min_value)
        t2 = torch.clamp_max(t1, self.max_value)
        v1 = torch.conv_transpose2d(x1, self.weight, bias=t2)
        return v1




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [3, 1, 1, 8], expected bias to be 1-dimensional with 1 elements, but got bias of size [8] instead

jit:
Failed running call_function <built-in method conv_transpose2d of type object at 0x73ab102699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 3, 64, 64)), Parameter(FakeTensor(..., device='cuda:0', size=(3, 1, 1, 8), requires_grad=True))), **{'bias': FakeTensor(..., device='cuda:0', size=(8,))}):
Given transposed=1, weight of size [3, 1, 1, 8], expected bias to be 1-dimensional with 1 elements, but got bias of size [8] instead

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''