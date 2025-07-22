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
        self.conv1 = torch.nn.Conv2d(1, 2, 3, stride=(2, 2), padding=(1, 1))
        self.conv2 = torch.nn.Conv2d(2, 4, 1, stride=1, padding=0)
        self.conv3 = torch.nn.Conv2d(4, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1) > 0
        v3 = self.conv2(v1) * 0.1
        v4 = self.conv3(torch.where(v2, v1, v3))
        return v4



func = Model().to('cpu')


x1 = torch.randn(1, 1, 512, 512)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (4) must match the size of tensor b (2) at non-singleton dimension 1

jit:
Failed running call_function <built-in method where of type object at 0x7e6841196ec0>(*(FakeTensor(..., size=(1, 4, 256, 256), dtype=torch.bool), FakeTensor(..., size=(1, 2, 256, 256)), FakeTensor(..., size=(1, 4, 256, 256))), **{}):
Attempting to broadcast a dimension of length 2 at -3! Mismatching argument at index 1 had torch.Size([1, 2, 256, 256]); but expected shape should be broadcastable to [1, 4, 256, 256]

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''