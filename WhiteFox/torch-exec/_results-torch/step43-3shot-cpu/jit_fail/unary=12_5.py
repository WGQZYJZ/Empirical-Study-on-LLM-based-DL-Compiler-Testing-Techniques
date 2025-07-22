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
        self.conv1 = torch.nn.Conv2d(3, 8, (1, 7), stride=1, padding=(0, 3))
        self.conv2 = torch.nn.Conv2d(8, 32, 3, stride=1, padding=1)
        self.sigmoid = torch.nn.Sigmoid()
        self.gelu = torch.nn.GELU()

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        v3 = self.sigmoid(v2) * x1
        v4 = self.gelu(v2) + x1
        return (v3, v4)



func = Model().to('cpu')


x1 = torch.randn(1, 3, 256, 128)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (32) must match the size of tensor b (3) at non-singleton dimension 1

jit:
Failed running call_function <built-in function mul>(*(FakeTensor(..., size=(1, 32, 256, 128)), FakeTensor(..., size=(1, 3, 256, 128))), **{}):
Attempting to broadcast a dimension of length 3 at -3! Mismatching argument at index 1 had torch.Size([1, 3, 256, 128]); but expected shape should be broadcastable to [1, 32, 256, 128]

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''