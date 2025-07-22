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
        self.conv = torch.nn.Conv2d(17, 10, 1, stride=1, padding=1, groups=1)

    def forward(self, x1, t1):
        v1 = self.conv(x1)
        if (t1 == True):
            t1 = torch.randn(v1.shape)
        v2 = (v1 + t1)
        return v2




func = Model().to('cuda')



x1 = torch.randn(3, 17, 64, 64)

t1 = 1

test_inputs = [x1, t1]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu!

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(3, 10, 66, 66)), FakeTensor(..., size=(3, 10, 66, 66))), **{}):
Unhandled FakeTensor Device Propagation for aten.add.Tensor, found two different devices cuda:0, cpu

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''