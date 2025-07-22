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
        self.conv = torch.nn.Conv2d(4, 4, 3, stride=1)
        self.conv2 = torch.nn.Conv2d(4, 4, 3, stride=1)
        self.conv3 = torch.nn.Conv2d(4, 4, 3, stride=1)
        self.conv4 = torch.nn.Conv2d(4, 4, 3, stride=1)
        self.conv5 = torch.nn.Conv2d(4, 4, 3, stride=1)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.conv2(v1)
        v3 = self.conv3(v2)
        v4 = self.conv4(v3)
        v5 = self.conv5(v4)
        v6 = (v5 * v5)
        v7 = (v1 + v6)
        v8 = (v7 * 0.7978845608028654)
        v9 = torch.tanh(v8)
        v10 = (v9 + 1)
        v11 = (v1 * v10)
        return v11




func = Model().to('cuda')



x1 = torch.randn(1, 4, 256, 256)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (254) must match the size of tensor b (246) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 4, 254, 254)), FakeTensor(..., device='cuda:0', size=(1, 4, 246, 246))), **{}):
Attempting to broadcast a dimension of length 246 at -1! Mismatching argument at index 1 had torch.Size([1, 4, 246, 246]); but expected shape should be broadcastable to [1, 4, 254, 254]

from user code:
   File "<string>", line 32, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''