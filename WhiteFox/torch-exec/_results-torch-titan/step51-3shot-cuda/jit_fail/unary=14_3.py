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
        self.conv2d_3 = torch.nn.Conv2d(226, 500, 3, stride=1, padding=0)
        self.conv2d_5 = torch.nn.Conv2d(500, 1000, 3, stride=1, padding=0)
        self.conv2d_7 = torch.nn.Conv2d(1000, 606, 2, stride=1, padding=0)
        self.transposeconv2d_10 = torch.nn.ConvTranspose2d(606, 400, 6, stride=9, padding=0)

    def forward(self, x1):
        v1 = self.conv2d_3(x1)
        v2 = torch.sigmoid(v1)
        v3 = (v1 * v2)
        v4 = self.conv2d_5(v3)
        v5 = torch.sigmoid(v4)
        v6 = (v4 * v5)
        v7 = self.conv2d_7(v6)
        v8 = torch.sigmoid(v7)
        v9 = (v1 * v4)
        v10 = self.transposeconv2d_10(v9)
        return v10




func = Model().to('cuda')



x1 = torch.randn(1, 226, 10, 10)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (8) must match the size of tensor b (6) at non-singleton dimension 3

jit:
Failed running call_function <built-in function mul>(*(FakeTensor(..., device='cuda:0', size=(1, 500, 8, 8)), FakeTensor(..., device='cuda:0', size=(1, 1000, 6, 6))), **{}):
Attempting to broadcast a dimension of length 6 at -1! Mismatching argument at index 1 had torch.Size([1, 1000, 6, 6]); but expected shape should be broadcastable to [1, 500, 8, 8]

from user code:
   File "<string>", line 33, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''