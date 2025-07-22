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
        self.conv_1 = torch.nn.Conv2d(3, 20, 5, stride=2, padding=2, bias=False)
        self.conv_2 = torch.nn.Conv2d(3, 20, 3, stride=1, padding=1, bias=False)

    def forward(self, x1):
        v1 = self.conv_1(x1)
        v2 = self.conv_2(x1)
        v3 = (v1 + v2)
        v4 = F.relu(v3)
        return v4




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (32) must match the size of tensor b (64) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 20, 32, 32)), FakeTensor(..., device='cuda:0', size=(1, 20, 64, 64))), **{}):
Attempting to broadcast a dimension of length 64 at -1! Mismatching argument at index 1 had torch.Size([1, 20, 64, 64]); but expected shape should be broadcastable to [1, 20, 32, 32]

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''