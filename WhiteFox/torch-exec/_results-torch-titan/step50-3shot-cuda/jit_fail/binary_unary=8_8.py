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
        self.conv1 = torch.nn.Conv2d(1, 4, 3, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(1, 8, 3, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = (v1 + self.conv2(x1))
        v3 = torch.relu(v2)
        v4 = (v1 + self.conv2(x1))
        v5 = torch.relu(v4)
        v6 = self.conv2(x1)
        v7 = (v3 + v6)
        v8 = self.conv2(x1)
        v9 = (v5 + v8)
        v10 = torch.relu(v9)
        v11 = self.conv2(x1)
        v12 = (v7 + v11)
        v13 = torch.relu(v12)
        return v13




func = Model().to('cuda')



x1 = torch.randn(1, 1, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (4) must match the size of tensor b (8) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 4, 64, 64)), FakeTensor(..., device='cuda:0', size=(1, 8, 64, 64))), **{}):
Attempting to broadcast a dimension of length 8 at -3! Mismatching argument at index 1 had torch.Size([1, 8, 64, 64]); but expected shape should be broadcastable to [1, 4, 64, 64]

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''