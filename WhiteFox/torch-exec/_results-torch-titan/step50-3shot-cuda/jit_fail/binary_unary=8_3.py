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
        self.conv1 = torch.nn.Conv2d(1, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(1, 16, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv1(x1)
        v3 = (v1 + v2)
        v4 = torch.relu(v3)
        v5 = self.conv2(x1)
        v6 = self.conv2(x1)
        v7 = (v5 + v6)
        v8 = torch.relu(v7)
        v9 = self.conv1(x1)
        v10 = self.conv1(x1)
        v11 = (v9 + v10)
        v12 = torch.relu(v11)
        v13 = ((v4 + v8) + v12)
        return v13




func = Model().to('cuda')



x1 = torch.randn(1, 1, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (8) must match the size of tensor b (16) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 8, 66, 66)), FakeTensor(..., device='cuda:0', size=(1, 16, 66, 66))), **{}):
Attempting to broadcast a dimension of length 16 at -3! Mismatching argument at index 1 had torch.Size([1, 16, 66, 66]); but expected shape should be broadcastable to [1, 8, 66, 66]

from user code:
   File "<string>", line 35, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''