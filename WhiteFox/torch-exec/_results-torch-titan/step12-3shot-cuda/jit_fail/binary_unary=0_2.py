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
        self.conv = torch.nn.Conv2d(1, 1, 13, stride=1, padding=0)
        self.conv1 = torch.nn.Conv2d(16, 16, 7, stride=1, padding=3)

    def forward(self, x1, x2, x3):
        v1 = self.conv(x1)
        v2 = (x3 * v1)
        v3 = self.conv1(x2)
        v4 = (v2 + v3)
        v5 = torch.relu(v4)
        return v5




func = Model().to('cuda')



x1 = torch.randn(1, 1, (15 * 13), (15 * 13))



x2 = torch.randn(1, 16, 64, 64)



x3 = torch.randn(1, 1, 13, 13)


test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
The size of tensor a (13) must match the size of tensor b (183) at non-singleton dimension 3

jit:
Failed running call_function <built-in function mul>(*(FakeTensor(..., device='cuda:0', size=(1, 1, 13, 13)), FakeTensor(..., device='cuda:0', size=(1, 1, 183, 183))), **{}):
Attempting to broadcast a dimension of length 183 at -1! Mismatching argument at index 1 had torch.Size([1, 1, 183, 183]); but expected shape should be broadcastable to [1, 1, 13, 13]

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''