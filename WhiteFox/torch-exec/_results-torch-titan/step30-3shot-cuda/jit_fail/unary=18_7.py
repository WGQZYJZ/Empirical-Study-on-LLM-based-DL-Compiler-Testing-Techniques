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
        self.conv1 = torch.nn.Conv2d(32, 32, kernel_size=(14, 17), stride=(12, 24), padding=(8, 10), groups=32)
        self.conv2 = torch.nn.Conv2d(32, 48, kernel_size=(10, 7), stride=(11, 13), padding=(7, 3))
        self.conv3 = torch.nn.Conv2d(48, 96, kernel_size=(10, 10), stride=(9, 10), padding=(7, 6))

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = torch.sigmoid(v1)
        v3 = self.conv2(v2)
        v4 = torch.sigmoid(v3)
        v5 = torch.sigmoid(v2)
        v6 = self.conv3((v4 + v5))
        v7 = torch.sigmoid(v6)
        return v7




func = Model().to('cuda')



x1 = torch.randn(1, 32, 152, 212)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (2) must match the size of tensor b (13) at non-singleton dimension 2

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 48, 2, 1)), FakeTensor(..., device='cuda:0', size=(1, 32, 13, 9))), **{}):
Attempting to broadcast a dimension of length 13 at -2! Mismatching argument at index 1 had torch.Size([1, 32, 13, 9]); but expected shape should be broadcastable to [1, 48, 2, 9]

from user code:
   File "<string>", line 29, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''