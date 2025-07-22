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
        self.conv1a = torch.nn.Conv2d(3, 3, 1)
        self.conv1b = torch.nn.Conv2d(3, 3, 2)

    def forward(self, x1):
        v1 = v2 = x1
        v3a = self.conv1a(x1)
        v4a = F.relu(v3a)
        v5a = torch.squeeze(v4a, 2)
        v3b = self.conv1b(x1)
        v4b = F.relu(v3b)
        v5b = torch.squeeze(v4b, 2)
        v6 = (v5a - v5b)
        return v6




func = Model().to('cuda')



x1 = torch.randn(3, 3, 3, 3)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (3) must match the size of tensor b (2) at non-singleton dimension 3

jit:
Failed running call_function <built-in function sub>(*(FakeTensor(..., device='cuda:0', size=(3, 3, 3, 3)), FakeTensor(..., device='cuda:0', size=(3, 3, 2, 2))), **{}):
Attempting to broadcast a dimension of length 2 at -1! Mismatching argument at index 1 had torch.Size([3, 3, 2, 2]); but expected shape should be broadcastable to [3, 3, 3, 3]

from user code:
   File "<string>", line 30, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''