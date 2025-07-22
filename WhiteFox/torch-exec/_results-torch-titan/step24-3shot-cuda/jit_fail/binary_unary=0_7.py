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
        self.conv1 = torch.nn.Conv2d(16, 16, 3, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(16, 16, 3, stride=1, padding=1)
        self.conv3 = torch.nn.Conv2d(16, 16, 2, stride=1, padding=0)

    def forward(self, x):
        v1 = self.conv1(x)
        v2 = self.conv2(x)
        v3 = self.conv3(x)
        v4 = (v1 + v2)
        v5 = torch.relu(v4)
        v6 = (v5 + v3)
        v7 = torch.relu(v6)
        return v7




func = Model().to('cuda')



x = torch.randn(2, 16, 64, 64)


test_inputs = [x]

# JIT_FAIL
'''
direct:
The size of tensor a (64) must match the size of tensor b (63) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(2, 16, 64, 64)), FakeTensor(..., device='cuda:0', size=(2, 16, 63, 63))), **{}):
Attempting to broadcast a dimension of length 63 at -1! Mismatching argument at index 1 had torch.Size([2, 16, 63, 63]); but expected shape should be broadcastable to [2, 16, 64, 64]

from user code:
   File "<string>", line 29, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''