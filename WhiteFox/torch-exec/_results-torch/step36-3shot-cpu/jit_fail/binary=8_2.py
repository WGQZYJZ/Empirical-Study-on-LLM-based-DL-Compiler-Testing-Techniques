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
        self.conv1 = torch.nn.Conv2d(256, 256, 3, stride=1, padding=1)

    def forward(self, u, key):
        t1 = self.conv1(key)
        t2 = self.conv1(key)
        t3 = self.conv1(key)
        t4 = u + t1
        t5 = u + t2
        t6 = u + t3
        t7 = t4 + t5
        t8 = t7 + t6
        return t8



func = Model().to('cpu')


u = torch.randn(1, 256, 128, 128)

key = torch.randn(1, 256, 64, 64)

test_inputs = [u, key]

# JIT_FAIL
'''
direct:
The size of tensor a (128) must match the size of tensor b (64) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(1, 256, 128, 128)), FakeTensor(..., size=(1, 256, 64, 64))), **{}):
Attempting to broadcast a dimension of length 64 at -1! Mismatching argument at index 1 had torch.Size([1, 256, 64, 64]); but expected shape should be broadcastable to [1, 256, 128, 128]

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''