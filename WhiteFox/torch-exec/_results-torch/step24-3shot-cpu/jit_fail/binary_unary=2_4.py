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
        self.conv1 = torch.nn.Conv2d(3, 16, 1, stride=2, padding=1)
        self.conv2 = torch.nn.Conv2d(16, 32, 3, stride=1, padding=1, groups=2)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        v3 = v1 - 0.06
        v4 = F.relu(v2 - torch.tanh(v3))
        return v4



func = Model().to('cpu')


x1 = torch.randn(1, 3, 256, 256)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (32) must match the size of tensor b (16) at non-singleton dimension 1

jit:
Failed running call_function <built-in function sub>(*(FakeTensor(..., size=(1, 32, 129, 129)), FakeTensor(..., size=(1, 16, 129, 129))), **{}):
Attempting to broadcast a dimension of length 16 at -3! Mismatching argument at index 1 had torch.Size([1, 16, 129, 129]); but expected shape should be broadcastable to [1, 32, 129, 129]

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''