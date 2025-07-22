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
        self.conv_transpose = torch.nn.ConvTranspose2d(1, 3, 3)

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = x1.permute(0, 3, 2, 1)
        v3 = (v1 + v2)
        v4 = torch.relu(v3)
        return v4




func = Model().to('cuda')



x1 = torch.randn(1, 1, 32, 32)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (34) must match the size of tensor b (32) at non-singleton dimension 2

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 3, 34, 34)), FakeTensor(..., device='cuda:0', size=(1, 32, 32, 1))), **{}):
Attempting to broadcast a dimension of length 32 at -2! Mismatching argument at index 1 had torch.Size([1, 32, 32, 1]); but expected shape should be broadcastable to [1, 3, 34, 34]

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''