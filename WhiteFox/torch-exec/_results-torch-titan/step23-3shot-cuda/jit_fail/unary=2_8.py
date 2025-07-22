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
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 3, 2, stride=1, padding=1)

    def forward(self, x1):
        v1 = (self.conv_transpose(x1) + x1)
        v2 = (v1 * 0.5)
        v3 = ((v1 * v1) * v1)
        v4 = (v3 * 0.044715)
        v5 = (v1 + v4)
        v6 = (v5 * 0.7978845608028654)
        v7 = torch.tanh(v6)
        v8 = (v7 + 1)
        v9 = (v2 * v8)
        return v9




func = Model().to('cuda')



x1 = torch.randn(3, 3, 8, 4)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (3) must match the size of tensor b (4) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(3, 3, 7, 3)), FakeTensor(..., device='cuda:0', size=(3, 3, 8, 4))), **{}):
Attempting to broadcast a dimension of length 4 at -1! Mismatching argument at index 1 had torch.Size([3, 3, 8, 4]); but expected shape should be broadcastable to [3, 3, 7, 3]

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''