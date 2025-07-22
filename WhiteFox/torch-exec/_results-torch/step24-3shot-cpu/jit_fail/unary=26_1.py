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
        self.conv_t = torch.nn.ConvTranspose2d(3, 49, 3, stride=1)

    def forward(self, x2):
        v1 = self.conv_t(x2)
        m1 = x2 > 0
        v2 = v1 * torch.where(m1, x2, m1)
        m2 = v2 < 5
        v5 = v2 * m2
        return v5



func = Model().to('cpu')


x2 = torch.randn(8, 3, 8, 8)

test_inputs = [x2]

# JIT_FAIL
'''
direct:
The size of tensor a (10) must match the size of tensor b (8) at non-singleton dimension 3

jit:
Failed running call_function <built-in function mul>(*(FakeTensor(..., size=(8, 49, 10, 10)), FakeTensor(..., size=(8, 3, 8, 8))), **{}):
Attempting to broadcast a dimension of length 8 at -1! Mismatching argument at index 1 had torch.Size([8, 3, 8, 8]); but expected shape should be broadcastable to [8, 49, 10, 10]

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''