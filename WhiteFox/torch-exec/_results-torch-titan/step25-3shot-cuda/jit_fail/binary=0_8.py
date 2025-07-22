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
        self.conv = torch.nn.Conv2d(64, 3, 1, stride=1, padding=1)

    def forward(self, x1, bias1=True, other=True, size1=None):
        v1 = self.conv(x1)
        if ((bias1 == True) or (other == True) or (size1 == True)):
            other = torch.randn(v1.shape)
        v2 = (v1 + other)
        return v2




func = Model().to('cuda')



x1 = torch.randn(32, 64, 4, 4)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu!

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(32, 3, 6, 6)), FakeTensor(..., size=(32, 3, 6, 6))), **{}):
Unhandled FakeTensor Device Propagation for aten.add.Tensor, found two different devices cuda:0, cpu

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''