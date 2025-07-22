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
        self.conv_t = torch.nn.ConvTranspose2d(476, 338, 2, stride=1, padding=0, bias=False)

    def forward(self, x5):
        v1 = self.conv_t(x5)
        v2 = (v1 > 0)
        v3 = (v1 * 0.4987)
        v4 = torch.where(v2, v1, v3)
        v5 = (v4 + torch.nn.functional.upsample_bilinear(v4, (13, 31)))
        return v4




func = Model().to('cuda')



x5 = torch.randn(13, 476, 6, 32)


test_inputs = [x5]

# JIT_FAIL
'''
direct:
The size of tensor a (33) must match the size of tensor b (31) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(13, 338, 7, 33)), FakeTensor(..., device='cuda:0', size=(13, 338, 13, 31))), **{}):
Attempting to broadcast a dimension of length 31 at -1! Mismatching argument at index 1 had torch.Size([13, 338, 13, 31]); but expected shape should be broadcastable to [13, 338, 7, 33]

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''