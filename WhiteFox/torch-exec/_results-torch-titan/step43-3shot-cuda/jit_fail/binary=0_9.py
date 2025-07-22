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
        self.conv = torch.nn.Conv2d(5, 1, 1, stride=1, padding=1)

    def forward(self, x1, other1=None, other2=None):
        v1 = self.conv(x1)
        if ((other1 is None) and (other2 is None)):
            other1 = torch.randn(v1.shape)
            other2 = torch.randn(v1.shape)
        v2 = (v1 + other1)
        v3 = (v2 + other2)
        return v3




func = Model().to('cuda')



x1 = torch.randn(1, 5, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu!

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 1, 66, 66)), FakeTensor(..., size=(1, 1, 66, 66))), **{}):
Unhandled FakeTensor Device Propagation for aten.add.Tensor, found two different devices cuda:0, cpu

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''