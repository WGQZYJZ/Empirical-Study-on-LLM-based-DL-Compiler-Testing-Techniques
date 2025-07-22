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
        self.conv_transpose = torch.nn.ConvTranspose2d(6, 56, 1, stride=(1, 2), padding=0)
        self.conv = torch.nn.Conv2d(6, 40, 1, stride=(1, 2), padding=0)

    def forward(self, x3):
        v1 = self.conv_transpose(x3)
        v2 = self.conv(x3)
        v3 = (v1 > 0)
        v4 = (v2 > 0)
        v5 = torch.logical_and(v3, v2)
        v6 = torch.logical_and(v4, v5)
        v7 = (v2 * 2.727)
        v8 = torch.where(v6, v1, v7)
        return v8




func = Model().to('cuda')



x3 = torch.randn(1, 6, 16, 8)


test_inputs = [x3]

# JIT_FAIL
'''
direct:
The size of tensor a (15) must match the size of tensor b (4) at non-singleton dimension 3

jit:
Failed running call_function <built-in method logical_and of type object at 0x7d5a0e6699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 56, 16, 15), dtype=torch.bool), FakeTensor(..., device='cuda:0', size=(1, 40, 16, 4))), **{}):
Attempting to broadcast a dimension of length 4 at -1! Mismatching argument at index 1 had torch.Size([1, 40, 16, 4]); but expected shape should be broadcastable to [1, 56, 16, 15]

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''