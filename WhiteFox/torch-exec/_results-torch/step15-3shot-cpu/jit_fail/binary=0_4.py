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
        self.relu = torch.nn.ReLU(inplace=False)
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv1 = torch.nn.Conv2d(8, 8, 3, stride=1, padding=3)

    def forward(self, x1, other=True, padding1=None):
        v1 = self.relu(self.conv(x1))
        if padding1 == None:
            x2 = self.conv1(v1)
        v2 = v1 + x2
        return v2



func = Model().to('cpu')


x1 = torch.randn(1, 3, 28, 28)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (30) must match the size of tensor b (34) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(1, 8, 30, 30)), FakeTensor(..., size=(1, 8, 34, 34))), **{}):
Attempting to broadcast a dimension of length 34 at -1! Mismatching argument at index 1 had torch.Size([1, 8, 34, 34]); but expected shape should be broadcastable to [1, 8, 30, 30]

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''