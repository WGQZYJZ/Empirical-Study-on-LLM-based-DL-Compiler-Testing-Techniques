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
        self.conv = torch.nn.Conv2d(56, 64, 1, stride=1, padding=1)

    def forward(self, x1, x2=None, other=None):
        if (x2 == None):
            x2 = torch.randn(x1.shape)
        v1 = self.conv(x1)
        if (other == None):
            other = torch.randn(v1.shape)
        v2 = (v1 * x2)
        v3 = (v2 + other)
        return v3




func = Model().to('cuda')



x1 = torch.randn(10, 56, 48, 48)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (50) must match the size of tensor b (48) at non-singleton dimension 3

jit:
Failed running call_function <built-in function mul>(*(FakeTensor(..., device='cuda:0', size=(10, 64, 50, 50)), FakeTensor(..., size=(10, 56, 48, 48))), **{}):
Attempting to broadcast a dimension of length 48 at -1! Mismatching argument at index 1 had torch.Size([10, 56, 48, 48]); but expected shape should be broadcastable to [10, 64, 50, 50]

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''