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
        self.conv = torch.nn.Conv2d(3, 9, 2, stride=2, padding=1, dilation=1)
        self.conv1 = torch.nn.Conv2d(4, 12, 2, stride=2, padding=1)
        self.conv2 = torch.nn.Conv2d(5, 12, 2, stride=2, padding=1)

    def forward(self, x1, x2, x3):
        v1 = self.conv(x1)
        v2 = self.conv1(x2)
        v3 = self.conv2(x3)
        v4 = ((v1 + v2) + v3)
        v5 = F.relu(v4)
        return v5




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)



x2 = torch.randn(1, 4, 32, 32)



x3 = torch.randn(1, 5, 16, 16)


test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
The size of tensor a (33) must match the size of tensor b (17) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 9, 33, 33)), FakeTensor(..., device='cuda:0', size=(1, 12, 17, 17))), **{}):
Attempting to broadcast a dimension of length 17 at -1! Mismatching argument at index 1 had torch.Size([1, 12, 17, 17]); but expected shape should be broadcastable to [1, 9, 33, 33]

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''