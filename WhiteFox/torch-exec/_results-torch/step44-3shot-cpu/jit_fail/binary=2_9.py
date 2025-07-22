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
        self.dense = torch.nn.Linear(16, 43)
        self.conv = torch.nn.Conv2d(28, 10, 3, stride=1, padding=1)

    def forward(self, x1, x2):
        v1 = F.relu(self.dense(x1))
        v2 = self.conv(x2)
        v3 = v1 - v2
        v4 = v3 - 0.23
        return v4



func = Model().to('cpu')


x1 = torch.randn(1, 16)

x2 = torch.randn(1, 28, 6, 6)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
The size of tensor a (43) must match the size of tensor b (6) at non-singleton dimension 3

jit:
Failed running call_function <built-in function sub>(*(FakeTensor(..., size=(1, 43)), FakeTensor(..., size=(1, 10, 6, 6))), **{}):
Attempting to broadcast a dimension of length 6 at -1! Mismatching argument at index 1 had torch.Size([1, 10, 6, 6]); but expected shape should be broadcastable to [1, 1, 1, 43]

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''