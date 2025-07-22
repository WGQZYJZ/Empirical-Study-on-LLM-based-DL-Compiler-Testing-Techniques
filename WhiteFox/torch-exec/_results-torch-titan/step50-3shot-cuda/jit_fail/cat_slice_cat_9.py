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

    def forward(self, x1, x2, x3, x4, x5, x6, x7, x8, x9):
        x1 = x1[:, :, :, 0:32]
        x2 = x2[:, :, :, 4:64]
        x3 = x3[:, :, :, 16:48]
        x4 = x4[:, :, :, 16:48]
        x5 = x5[:, :, :, 16:48]
        x6 = x6[:, :, :, 32:48]
        x7 = x7[:, :, :, 0:32]
        x8 = x8[:, :, :, 16:48]
        x9 = x9[:, :, :, 0:32]
        x0 = [x6, x1, x7, x9, x5, x3, x4, x2, x8]
        v1 = torch.cat(x0, dim=1)
        v2 = v1[:, 0:9223372036854775807]
        v3 = v2[:, 0:12]
        v4 = torch.cat([v1, v3], dim=1)
        return v4



func = Model().to('cuda')



x1 = torch.randn(1, 13, 16, 32)



x2 = torch.randn(1, 6, 16, 48)



x3 = torch.randn(1, 5, 16, 48)



x4 = torch.randn(1, 6, 16, 48)



x5 = torch.randn(1, 6, 16, 48)



x6 = torch.randn(1, 11, 16, 48)



x7 = torch.randn(1, 13, 16, 32)



x8 = torch.randn(1, 6, 16, 48)



x9 = torch.randn(1, 13, 16, 32)


test_inputs = [x1, x2, x3, x4, x5, x6, x7, x8, x9]

# JIT_FAIL
'''
direct:
Sizes of tensors must match except in dimension 1. Expected size 16 but got size 32 for tensor number 1 in the list.

jit:
Failed running call_function <built-in method cat of type object at 0x75ff78e699e0>(*([FakeTensor(..., device='cuda:0', size=(1, 11, 16, 16)), FakeTensor(..., device='cuda:0', size=(1, 13, 16, 32)), FakeTensor(..., device='cuda:0', size=(1, 13, 16, 32)), FakeTensor(..., device='cuda:0', size=(1, 13, 16, 32)), FakeTensor(..., device='cuda:0', size=(1, 6, 16, 32)), FakeTensor(..., device='cuda:0', size=(1, 5, 16, 32)), FakeTensor(..., device='cuda:0', size=(1, 6, 16, 32)), FakeTensor(..., device='cuda:0', size=(1, 6, 16, 44)), FakeTensor(..., device='cuda:0', size=(1, 6, 16, 32))],), **{'dim': 1}):
Sizes of tensors must match except in dimension 1. Expected 16 but got 32 for tensor number 1 in the list

from user code:
   File "<string>", line 31, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''