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
        self.conv2d_42 = torch.nn.Conv2d(in_channels=2, out_channels=2, kernel_size=(1, 2), stride=(1, 2), groups=2)
        self.conv2d_5689 = torch.nn.Conv2d(in_channels=2, out_channels=2, kernel_size=(1, 2), stride=(1, 2), groups=2)

    def forward(self, x):
        y = self.conv2d_42(x)
        p = torch.flatten(y, start_dim=2)
        r = torch.flatten(y, start_dim=2)
        s = p - r
        t = s + y
        u = self.conv2d_5689(t)
        return torch.flatten(t, start_dim=2)



func = Model().to('cpu')


x = torch.randn(1, 2, 6, 6)

test_inputs = [x]

# JIT_FAIL
'''
direct:
The size of tensor a (18) must match the size of tensor b (3) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(1, 2, 18)), FakeTensor(..., size=(1, 2, 6, 3))), **{}):
Attempting to broadcast a dimension of length 3 at -1! Mismatching argument at index 1 had torch.Size([1, 2, 6, 3]); but expected shape should be broadcastable to [1, 1, 2, 18]

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''