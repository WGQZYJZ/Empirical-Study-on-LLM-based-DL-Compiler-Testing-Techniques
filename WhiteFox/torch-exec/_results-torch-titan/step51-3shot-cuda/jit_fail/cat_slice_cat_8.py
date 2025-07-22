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

    def forward(self, x1, x2, x3, x4, x5, x6):
        v1 = [x1, x2, x3, x4, x5, x6]
        v2 = torch.cat(v1, dim=1)
        v3 = v2[:, 0:9223372036854775807]
        v4 = v3[:, 0:(x3.size(2) / 2)]
        return torch.cat([v2, v4], dim=1)



func = Model().to('cuda')



x1 = torch.randn(1, 64, 64, 64)



x2 = torch.randn(1, 64, 64, 64)



x3 = torch.randn(1, 32, 32, 64)



x4 = torch.randn(1, 32, 32, 64)



x5 = torch.randn(1, 32, 16, 64)



x6 = torch.randn(1, 32, 16, 64)


test_inputs = [x1, x2, x3, x4, x5, x6]

# JIT_FAIL
'''
direct:
Sizes of tensors must match except in dimension 1. Expected size 64 but got size 32 for tensor number 2 in the list.

jit:
Failed running call_function <built-in method cat of type object at 0x779e520699e0>(*([FakeTensor(..., device='cuda:0', size=(1, 64, 64, 64)), FakeTensor(..., device='cuda:0', size=(1, 64, 64, 64)), FakeTensor(..., device='cuda:0', size=(1, 32, 32, 64)), FakeTensor(..., device='cuda:0', size=(1, 32, 32, 64)), FakeTensor(..., device='cuda:0', size=(1, 32, 16, 64)), FakeTensor(..., device='cuda:0', size=(1, 32, 16, 64))],), **{'dim': 1}):
Sizes of tensors must match except in dimension 1. Expected 64 but got 32 for tensor number 2 in the list

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''