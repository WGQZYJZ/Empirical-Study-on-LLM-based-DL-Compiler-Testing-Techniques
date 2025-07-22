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
        self.conv = torch.nn.Conv2d(1, 3, 3, stride=1, padding=2)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 - 0.5
        t0 = torch.tensor([[[[-0.4566]], [[-0.4566]], [[-0.4566]]]]).to('cuda')
        v3 = t0 + v1
        return F.softmax(v3)



func = Model().to('cpu')


x1 = torch.randn(1, 1, 8, 8).to('cuda')

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu!

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 3, 1, 1)), FakeTensor(..., size=(1, 3, s0 + 2, s1 + 2))), **{}):
Tensor on device cpu is not on the expected device cuda:0!

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''