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

    def __init__(self, negative_slope1=0.01, negative_slope2=0.01):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(3, 8, 3, stride=1, padding=1)
        self.conv3 = torch.nn.Conv2d(3, 8, 5, stride=1, padding=1)
        self.negative_slope1 = negative_slope1
        self.negative_slope2 = negative_slope2

    def forward(self, x1, x2, x3):
        v1 = self.conv1(x1)
        v2 = (v1 > 0)
        v3 = (v1 * self.negative_slope1)
        v4 = torch.where(v2, v1, v3)
        v5 = self.conv2(x2)
        v6 = (v1 > 0)
        v7 = (v1 * self.negative_slope2)
        v8 = torch.where(v2, v5, v7)
        v9 = self.conv3(x3)
        v10 = (v1 > 0)
        v11 = (v1 * self.negative_slope2)
        v12 = torch.where(v2, v9, v11)
        return ((v4 + v8) + v12)




func = Model().to('cuda')



x1 = torch.randn(2, 3, 64, 64)



x2 = torch.randn(2, 3, 256, 256)



x3 = torch.randn(1, 3, 128, 128)


test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
The size of tensor a (66) must match the size of tensor b (256) at non-singleton dimension 3

jit:
Failed running call_function <built-in method where of type object at 0x71cefbc699e0>(*(FakeTensor(..., device='cuda:0', size=(2, 8, 66, 66), dtype=torch.bool), FakeTensor(..., device='cuda:0', size=(2, 8, 256, 256)), FakeTensor(..., device='cuda:0', size=(2, 8, 66, 66))), **{}):
Attempting to broadcast a dimension of length 256 at -1! Mismatching argument at index 1 had torch.Size([2, 8, 256, 256]); but expected shape should be broadcastable to [2, 8, 66, 66]

from user code:
   File "<string>", line 33, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''