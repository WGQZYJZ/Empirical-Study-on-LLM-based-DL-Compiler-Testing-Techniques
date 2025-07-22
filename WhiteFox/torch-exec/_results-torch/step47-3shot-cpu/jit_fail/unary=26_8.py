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
        self.conv_t = torch.nn.ConvTranspose2d(256, 512, 4, stride=2, padding=1, bias=False)

    def forward(self, x16, x17):
        o1 = self.conv_t(x16)
        o2 = o1 + x17
        o3 = o2 > 0
        o4 = torch.where(o3, o1, o2)
        return o4



func = Model().to('cpu')


x16 = torch.randn(3, 256, 26, 26)

x17 = torch.randn(3, 512, 7, 7)

test_inputs = [x16, x17]

# JIT_FAIL
'''
direct:
The size of tensor a (52) must match the size of tensor b (7) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(3, 512, 52, 52)), FakeTensor(..., size=(3, 512, 7, 7))), **{}):
Attempting to broadcast a dimension of length 7 at -1! Mismatching argument at index 1 had torch.Size([3, 512, 7, 7]); but expected shape should be broadcastable to [3, 512, 52, 52]

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''