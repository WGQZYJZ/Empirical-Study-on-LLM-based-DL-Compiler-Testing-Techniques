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
        self.conv1 = torch.nn.Conv2d(16, 16, 7, stride=1, padding=3)
        self.conv2 = torch.nn.Conv2d(16, 16, 7, stride=1, padding=6)

    def forward(self, x):
        v = self.conv1(x)
        v1 = (v + x)
        v2 = self.conv2(v1)
        v3 = (v2 + v1)
        v4 = torch.relu(v3)
        return v4




func = Model().to('cuda')



x = torch.randn(2, 16, 64, 64)


test_inputs = [x]

# JIT_FAIL
'''
direct:
The size of tensor a (70) must match the size of tensor b (64) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(2, 16, 70, 70)), FakeTensor(..., device='cuda:0', size=(2, 16, 64, 64))), **{}):
Attempting to broadcast a dimension of length 64 at -1! Mismatching argument at index 1 had torch.Size([2, 16, 64, 64]); but expected shape should be broadcastable to [2, 16, 70, 70]

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''