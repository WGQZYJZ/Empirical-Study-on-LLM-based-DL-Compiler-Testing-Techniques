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
        self.conv_1 = torch.nn.Conv2d(3, 12, 4, stride=4, padding=2, dilation=1)
        self.conv_2 = torch.nn.Conv2d(12, 64, 1, stride=1, padding=0)
        self.conv_3 = torch.nn.Conv2d(3, 64, 3, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv_1(x1)
        v2 = F.sigmoid(v1)
        v3 = (v1 * v2)
        v4 = self.conv_2(v1)
        v5 = F.sigmoid(v4)
        v6 = self.conv_3(x1)
        v7 = ((v6 * v5) + (v3 * v2))
        return v7




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (64) must match the size of tensor b (17) at non-singleton dimension 3

jit:
Failed running call_function <built-in function mul>(*(FakeTensor(..., device='cuda:0', size=(1, 64, 64, 64)), FakeTensor(..., device='cuda:0', size=(1, 64, 17, 17))), **{}):
Attempting to broadcast a dimension of length 17 at -1! Mismatching argument at index 1 had torch.Size([1, 64, 17, 17]); but expected shape should be broadcastable to [1, 64, 64, 64]

from user code:
   File "<string>", line 30, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''