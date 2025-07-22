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



class ModelTanh(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 1, (1,), 1, 0, bias=True)
        self.tanh = torch.nn.Tanh()

    def forward(self, x):
        v1 = self.conv(x)
        v2 = self.tanh(v1)
        b1 = (3 ** 4)
        b2 = (len(set(str(x))) - x.size(0))
        v3 = ((v2 * b1) + b2)
        v4 = (v3 / v3)
        return v4




func = ModelTanh().to('cuda')



x = torch.randn(238, 1, 15, 26)


test_inputs = [x]

# JIT_FAIL
'''
direct:
expected stride to be a single integer value or a list of 1 values to match the convolution dimensions, but got stride=[1, 1]

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(238, 1, 15, 26)),), **{}):
tuple index out of range

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''