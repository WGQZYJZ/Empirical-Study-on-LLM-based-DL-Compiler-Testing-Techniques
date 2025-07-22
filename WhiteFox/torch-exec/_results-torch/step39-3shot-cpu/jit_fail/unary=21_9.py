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

class ModelTanh(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(2, 16, (1, 2), (2, 1), (1, 2))
        self.conv2 = torch.nn.Conv2d(16, 16, (2, 1), padding=(3, 1), dilation=(2, 1))

    def forward(self, x):
        v1 = torch.add(self.conv(x), self.conv2(self.conv(x)))
        v2 = torch.tanh(v1)
        return v2



func = ModelTanh().to('cpu')


input = torch.randn(4, 2, 10, 20)

test_inputs = [input]

# JIT_FAIL
'''
direct:
The size of tensor a (23) must match the size of tensor b (25) at non-singleton dimension 3

jit:
Failed running call_function <built-in method add of type object at 0x783b08596ec0>(*(FakeTensor(..., size=(4, 16, 6, 23)), FakeTensor(..., size=(4, 16, 10, 25))), **{}):
Attempting to broadcast a dimension of length 25 at -1! Mismatching argument at index 1 had torch.Size([4, 16, 10, 25]); but expected shape should be broadcastable to [4, 16, 6, 23]

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''