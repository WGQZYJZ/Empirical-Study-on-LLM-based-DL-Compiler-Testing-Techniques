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
        self.conv = torch.nn.Conv2d(8, 8, 3, stride=2, padding=1)

    def forward(self, x):
        a = torch.nn.Parameter(torch.Tensor([0.1]))
        v1 = self.conv(x)
        v2 = (v1 > a)
        v3 = (v1 * a)
        v4 = torch.where(v2, v1, v3)
        return v4




func = Model().to('cuda')



x1 = torch.randn(1, 8, 96, 96)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu!

jit:
Failed running call_function <built-in function gt>(*(FakeTensor(..., device='cuda:0', size=(1, 8, 48, 48)), Parameter(FakeTensor(..., size=(1,), requires_grad=True))), **{}):
Unhandled FakeTensor Device Propagation for aten.gt.Tensor, found two different devices cuda:0, cpu

from user code:
   File "<string>", line 24, in <resume in forward>


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''