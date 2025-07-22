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
        self.conv = torch.nn.Conv2d(9, 6, 1, stride=1, padding=1)

    def forward(self, input=None, padding1=None, other=None, t3=None):
        if (input is None):
            input = torch.randn(1, 9, 64, 64)
        x1 = self.conv(input)
        if (other == None):
            other = torch.randn(x1.shape)
        v2 = (x1 + other)
        if (padding1 == None):
            padding1 = torch.randn(v2.shape)
        v3 = (v2 + padding1)
        if (t3 == None):
            t3 = torch.randn(v3.shape)
        v4 = (v3 + t3)
        return v4




func = Model().to('cuda')



input = torch.randn(1, 9, 64, 64)


test_inputs = [input]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu!

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 6, 66, 66)), FakeTensor(..., size=(1, 6, 66, 66))), **{}):
Unhandled FakeTensor Device Propagation for aten.add.Tensor, found two different devices cuda:0, cpu

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''