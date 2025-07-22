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
        self.conv_transpose1 = torch.nn.ConvTranspose2d(1, 4, 2, stride=2)
        self.conv_transpose2 = torch.nn.ConvTranspose2d(4, 1, 7, stride=2)

    def forward(self, x1):
        v1 = self.conv_transpose1(x1)
        v2 = self.conv_transpose2(v1) + 3
        v3 = torch.clamp(v2, min=0)
        v4 = torch.clamp(v3, max=6)
        v5 = v1 * v4
        v6 = v5 / 6
        return v6



func = Model().to('cpu')


x1 = torch.randn(1, 1, 10, 10)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (20) must match the size of tensor b (45) at non-singleton dimension 3

jit:
Failed running call_function <built-in function mul>(*(FakeTensor(..., size=(1, 4, 20, 20)), FakeTensor(..., size=(1, 1, 45, 45))), **{}):
Attempting to broadcast a dimension of length 45 at -1! Mismatching argument at index 1 had torch.Size([1, 1, 45, 45]); but expected shape should be broadcastable to [1, 4, 20, 20]

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''