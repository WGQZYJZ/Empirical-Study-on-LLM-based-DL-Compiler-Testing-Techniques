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
        self.conv0 = torch.nn.Conv2d(3, 8, 3, stride=1, padding=3)
        self.conv1 = torch.nn.Conv2d(3, 8, 3, stride=1, padding=1)
        self.sigmoid = torch.nn.Sigmoid()
        self.adaptiveavgpool2d = torch.nn.AdaptiveAvgPool2d((1, 1))

    def forward(self, x0, x1):
        v0 = self.conv0(x0)
        v2 = self.conv1(x1)
        v1 = (v0 - v2)
        v4 = self.sigmoid(v1)
        v5 = self.adaptiveavgpool2d(v1)
        return v4




func = Model().to('cuda')



x0 = torch.randn(1, 3, 64, 64)



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x0, x1]

# JIT_FAIL
'''
direct:
The size of tensor a (68) must match the size of tensor b (64) at non-singleton dimension 3

jit:
Failed running call_function <built-in function sub>(*(FakeTensor(..., device='cuda:0', size=(1, 8, 68, 68)), FakeTensor(..., device='cuda:0', size=(1, 8, 64, 64))), **{}):
Attempting to broadcast a dimension of length 64 at -1! Mismatching argument at index 1 had torch.Size([1, 8, 64, 64]); but expected shape should be broadcastable to [1, 8, 68, 68]

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''