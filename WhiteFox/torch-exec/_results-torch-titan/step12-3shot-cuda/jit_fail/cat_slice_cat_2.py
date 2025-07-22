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

    def forward(self, x1, x2, x3, x4, size):
        v1 = torch.cat([x1, x2, x3, x4], dim=1)
        v2 = v1[:, 0:9223372036854775807]
        v3 = v2[:, 0:size]
        v4 = torch.cat([v1, v3], dim=1)
        return v4



func = Model().to('cuda')



x1 = torch.randn(1, 14337, 32, 64)



x2 = torch.randn(1, 24557, 16, 32)



x3 = torch.randn(1, 34549, 8, 16)



x4 = torch.randn(1, 19345, 4, 8)



size = torch.randint(low=0, high=24557, size=(1,))


test_inputs = [x1, x2, x3, x4, size]

# JIT_FAIL
'''
direct:
Sizes of tensors must match except in dimension 1. Expected size 32 but got size 16 for tensor number 1 in the list.

jit:
Failed running call_function <built-in method cat of type object at 0x71c1d2c699e0>(*([FakeTensor(..., device='cuda:0', size=(1, 14337, 32, 64)), FakeTensor(..., device='cuda:0', size=(1, 24557, 16, 32)), FakeTensor(..., device='cuda:0', size=(1, 34549, 8, 16)), FakeTensor(..., device='cuda:0', size=(1, 19345, 4, 8))],), **{'dim': 1}):
Sizes of tensors must match except in dimension 1. Expected 32 but got 16 for tensor number 1 in the list

from user code:
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''