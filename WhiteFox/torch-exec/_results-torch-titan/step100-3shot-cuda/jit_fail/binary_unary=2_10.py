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
        self.relu = torch.nn.ReLU()
        self.conv1 = torch.nn.ConvTranspose2d(1, 1, 3, 2, 1, 1)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.relu(v1)
        v3 = (v2 - torch.full((1, 1, 8, 8), 0.0, dtype=torch.float))
        v4 = self.relu(v3)
        v5 = (v4 - torch.full((1, 1, 8, 8), (- 0.1), dtype=torch.float))
        v6 = self.relu(v5)
        return v6




func = Model().to('cuda')



x1 = torch.randn(1, 1, 8, 8)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (16) must match the size of tensor b (8) at non-singleton dimension 3

jit:
Failed running call_function <built-in function sub>(*(FakeTensor(..., device='cuda:0', size=(1, 1, 16, 16)), FakeTensor(..., size=(1, 1, 8, 8))), **{}):
Attempting to broadcast a dimension of length 8 at -1! Mismatching argument at index 1 had torch.Size([1, 1, 8, 8]); but expected shape should be broadcastable to [1, 1, 16, 16]

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''