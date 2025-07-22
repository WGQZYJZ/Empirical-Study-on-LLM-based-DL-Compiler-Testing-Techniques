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
        self.conv1 = torch.nn.Conv2d(3, 6, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(3, 6, 3, stride=1, padding=1)
        self.conv3 = torch.nn.Conv2d(6, 3, 3, stride=1, padding=1)
        self.conv4 = torch.nn.Conv2d(3, 6, 3, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(x1)
        v3 = (v2 + v1)
        v4 = torch.clamp(v3, 0, 6)
        v5 = self.conv3(v4)
        v6 = (v4 * v5)
        v7 = (v6 / 6)
        v8 = self.conv4(v7)
        return v8




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (64) must match the size of tensor b (66) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 6, 64, 64)), FakeTensor(..., device='cuda:0', size=(1, 6, 66, 66))), **{}):
Attempting to broadcast a dimension of length 66 at -1! Mismatching argument at index 1 had torch.Size([1, 6, 66, 66]); but expected shape should be broadcastable to [1, 6, 64, 64]

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''