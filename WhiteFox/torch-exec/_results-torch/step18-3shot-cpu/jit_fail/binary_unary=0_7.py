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

    def forward(self, x1, x2):
        x0 = torch.nn.functional.pad(x1, pad=(3, 3, 3, 3))
        x3 = torch.nn.functional.relu(x0)
        x4 = torch.nn.functional.conv2d(x3, weight=x2, stride=(1, 1), padding=(3, 3))
        x5 = x4 + x1
        x6 = torch.nn.functional.relu(x5)
        l0 = torch.nn.functional.padding(x1, pad=(3, 3, 3, 3))
        l3 = torch.nn.functional.relu(l0)
        l4 = torch.nn.functional.conv2d(l3, weight=x2, stride=(1, 1), padding=(3, 3))
        l5 = l4 + x1
        l6 = torch.nn.functional.relu(l5)
        y = torch.nn.functional.conv2d(l6, weight=x2, stride=(1, 1), padding=(1, 1))
        return y



func = Model().to('cpu')


x1 = torch.randn(1, 16, 64, 64)

x2 = torch.randn(1, 16, 3, 3)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
The size of tensor a (74) must match the size of tensor b (64) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(1, 1, 74, 74)), FakeTensor(..., size=(1, 16, 64, 64))), **{}):
Attempting to broadcast a dimension of length 64 at -1! Mismatching argument at index 1 had torch.Size([1, 16, 64, 64]); but expected shape should be broadcastable to [1, 1, 74, 74]

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''