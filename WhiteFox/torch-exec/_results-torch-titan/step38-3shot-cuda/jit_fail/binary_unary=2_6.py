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
        self.conv1 = torch.nn.Conv2d(16, 32, 3)
        self.conv2 = torch.nn.Conv2d(32, 16, 3, padding=3, dilation=3)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        v3 = (v2 - 125.234)
        v4 = F.relu(v3)
        return (v4 + self.conv1(x1))




func = Model().to('cuda')



x1 = torch.randn(1, 16, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (16) must match the size of tensor b (32) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 16, 62, 62)), FakeTensor(..., device='cuda:0', size=(1, 32, 62, 62))), **{}):
Attempting to broadcast a dimension of length 32 at -3! Mismatching argument at index 1 had torch.Size([1, 32, 62, 62]); but expected shape should be broadcastable to [1, 16, 62, 62]

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''