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
        self.conv1 = torch.nn.Conv2d(4, 12, 3, stride=4, padding=2)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = v1 - 1
        v3 = F.relu(v2)
        v4 = torch.add(v3, x1)
        v5 = v4.view(1, 48, 10, 10)
        return v5



func = Model().to('cpu')


x1 = torch.randn(1, 4, 26, 26)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (7) must match the size of tensor b (26) at non-singleton dimension 3

jit:
Failed running call_function <built-in method add of type object at 0x7e29b6396ec0>(*(FakeTensor(..., size=(1, 12, 7, 7)), FakeTensor(..., size=(1, 4, 26, 26))), **{}):
Attempting to broadcast a dimension of length 26 at -1! Mismatching argument at index 1 had torch.Size([1, 4, 26, 26]); but expected shape should be broadcastable to [1, 12, 7, 7]

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''