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

    def __init__(self, in_channels, out_channels, kernel_size, stride, padding):
        super().__init__()
        self.linear1 = torch.nn.Linear(in_features=in_channels, bias=False, out_features=out_channels)
        self.linear2 = torch.nn.Linear(in_features=out_channels, bias=False, out_features=out_channels)

    def forward(self, x1):
        v1 = self.linear1(x1)
        v2 = torch.sigmoid(v1)
        v3 = self.linear2(v2)
        v4 = torch.sigmoid(v3)
        return v4




in_channels = 3


out_channels = 128


kernel_size = 1


stride = 1


padding = 1


func = Model(in_channels, out_channels, kernel_size, stride, padding).to('cuda')



x1 = torch.randn(3, 8, 12, 4)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (288x4 and 3x128)

jit:
Failed running call_module L__self___linear1(*(FakeTensor(..., device='cuda:0', size=(3, 8, 12, 4)),), **{}):
a and b must have same reduction dim, but got [288, 4] X [3, 128].

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''