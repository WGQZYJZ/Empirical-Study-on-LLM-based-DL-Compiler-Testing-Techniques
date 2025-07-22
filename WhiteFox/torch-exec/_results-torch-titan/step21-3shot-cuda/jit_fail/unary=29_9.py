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

    def __init__(self, min_value=100, max_value=1000):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(1, 16, 2, stride=2, padding=2)
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = torch.clamp_min(v1, self.min_value)
        v3 = torch.clamp_max(v2, self.max_value)
        v4 = torch.rand(1, 1, 5, 5)
        v5 = (v3 + v4)
        return v5




func = Model().to('cuda')



x1 = torch.randn(1, 1, 5, 5)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (6) must match the size of tensor b (5) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 16, 6, 6)), FakeTensor(..., size=(1, 1, 5, 5))), **{}):
Attempting to broadcast a dimension of length 5 at -1! Mismatching argument at index 1 had torch.Size([1, 1, 5, 5]); but expected shape should be broadcastable to [1, 16, 6, 6]

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''