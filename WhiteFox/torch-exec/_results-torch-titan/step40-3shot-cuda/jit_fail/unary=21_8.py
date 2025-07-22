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



class ModelTanh(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(6, 6, 1)
        self.conv2 = torch.nn.Conv2d(6, 12, 1)
        self.conv3 = torch.nn.Conv2d(12, 9, 1)
        self.conv4 = torch.nn.Conv2d(9, 9, 3)
        self.conv5 = torch.nn.Conv2d(9, 7, 3)

    def forward(self, x):
        v1 = self.conv(x)
        v2 = torch.tanh(v1)
        v3 = self.conv2(v2)
        v4 = torch.tanh(v3)
        v5 = self.conv3(v4)
        v6 = torch.tanh(v5)
        v7 = self.conv4(v6)
        v8 = (v7 + v1)
        v9 = self.conv5(v8)
        return v9




func = ModelTanh().to('cuda')



x = torch.randn(3, 6, 30, 10)


test_inputs = [x]

# JIT_FAIL
'''
direct:
The size of tensor a (8) must match the size of tensor b (10) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(3, 9, 28, 8)), FakeTensor(..., device='cuda:0', size=(3, 6, 30, 10))), **{}):
Attempting to broadcast a dimension of length 10 at -1! Mismatching argument at index 1 had torch.Size([3, 6, 30, 10]); but expected shape should be broadcastable to [3, 9, 28, 8]

from user code:
   File "<string>", line 33, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''