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
        self.conv_transpose = torch.nn.ConvTranspose2d(2, 7, 4, stride=2, padding=1)

    def forward(self, x1, x2):
        v1 = torch.add(self.conv_transpose(x1), x2)
        v2 = (v1 * 0.5)
        v3 = (v1 * 0.7071067811865476)
        v4 = torch.erf(v3)
        v5 = (v4 + 1)
        v6 = (v2 * v5)
        return v6




func = Model().to('cuda')



x1 = torch.randn(1, 2, 64, 64)



x2 = torch.randn(1, 7, 32, 32)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
The size of tensor a (128) must match the size of tensor b (32) at non-singleton dimension 3

jit:
Failed running call_function <built-in method add of type object at 0x7aa3238699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 7, 128, 128)), FakeTensor(..., device='cuda:0', size=(1, 7, 32, 32))), **{}):
Attempting to broadcast a dimension of length 32 at -1! Mismatching argument at index 1 had torch.Size([1, 7, 32, 32]); but expected shape should be broadcastable to [1, 7, 128, 128]

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''