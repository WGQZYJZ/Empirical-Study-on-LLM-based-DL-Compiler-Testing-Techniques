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
        self.conv1 = torch.nn.Conv2d(5, 6, 3, stride=1, padding=0)
        self.conv2 = torch.nn.Conv2d(6, 1, 1, stride=1, padding=0)
        self.conv3 = torch.nn.Conv2d(5, 6, 1, stride=1, padding=0)
        self.conv4 = torch.nn.Conv2d(6, 1, 1, stride=1, padding=0)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        v3 = torch.sigmoid(v2)
        v4 = self.conv3(x1)
        v5 = self.conv4(v4)
        v6 = torch.sigmoid(v5)
        v7 = (v3 * v6)
        return v7




func = Model().to('cuda')



x1 = torch.randn(1, 5, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (62) must match the size of tensor b (64) at non-singleton dimension 3

jit:
Failed running call_function <built-in function mul>(*(FakeTensor(..., device='cuda:0', size=(1, 1, 62, 62)), FakeTensor(..., device='cuda:0', size=(1, 1, 64, 64))), **{}):
Attempting to broadcast a dimension of length 64 at -1! Mismatching argument at index 1 had torch.Size([1, 1, 64, 64]); but expected shape should be broadcastable to [1, 1, 62, 62]

from user code:
   File "<string>", line 31, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''