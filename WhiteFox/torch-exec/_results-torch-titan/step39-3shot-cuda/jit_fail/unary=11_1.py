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
        self.conv2d = torch.nn.Conv2d(3, 32, 3, stride=2)
        self.conv_transpose = torch.nn.ConvTranspose2d(32, 16, 3, stride=2, padding=1)

    def forward(self, x1):
        v1 = self.conv2d(x1)
        v2 = self.conv_transpose(v1)
        v3 = (v2 + 3)
        v4 = torch.clamp_min(v3, 0)
        v5 = torch.clamp_max(v4, 6)
        v6 = (v5 / 6)
        return (v1 + v6)




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (31) must match the size of tensor b (61) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 32, 31, 31)), FakeTensor(..., device='cuda:0', size=(1, 16, 61, 61))), **{}):
Attempting to broadcast a dimension of length 61 at -1! Mismatching argument at index 1 had torch.Size([1, 16, 61, 61]); but expected shape should be broadcastable to [1, 32, 31, 31]

from user code:
   File "<string>", line 29, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''