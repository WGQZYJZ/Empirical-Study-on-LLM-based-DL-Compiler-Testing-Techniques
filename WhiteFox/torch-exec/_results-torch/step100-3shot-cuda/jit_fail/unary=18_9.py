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
        self.conv = torch.nn.Conv2d(3, 4, 1, 3, padding=2)

    def forward(self, x):
        return torch.sigmoid(self.conv(x)) * 3 + torch.ones(1, 1, 4, 4) ** 2



func = Model().to('cuda')


x = torch.randn(1, 3, 32, 32)

test_inputs = [x]

# JIT_FAIL
'''
direct:
The size of tensor a (12) must match the size of tensor b (4) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 4, 12, 12)), FakeTensor(..., size=(1, 1, 4, 4))), **{}):
Attempting to broadcast a dimension of length 4 at -1! Mismatching argument at index 1 had torch.Size([1, 1, 4, 4]); but expected shape should be broadcastable to [1, 4, 12, 12]

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''