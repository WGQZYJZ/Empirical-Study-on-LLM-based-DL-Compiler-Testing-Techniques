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

    def forward(self, x1, x2, padding1=None):
        v1 = torch.nn.functional.interpolate(x1, x2.shape[2:], mode='bicubic')
        if (padding1 == None):
            padding1 = torch.randn(v1.shape)
        v2 = (v1 + x2)
        return v2




func = Model().to('cuda')



x1 = torch.randn((1, 3, 32, 32))



x2 = torch.randn((1, 64, 32, 32))


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
The size of tensor a (3) must match the size of tensor b (64) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 3, 32, 32)), FakeTensor(..., device='cuda:0', size=(1, 64, 32, 32))), **{}):
Attempting to broadcast a dimension of length 64 at -3! Mismatching argument at index 1 had torch.Size([1, 64, 32, 32]); but expected shape should be broadcastable to [1, 3, 32, 32]

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''