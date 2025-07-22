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

    def __init__(self, size1, size2):
        super().__init__()
        self.size1 = size1
        self.size2 = size2

    def forward(self, x1, x2, x3):
        v0 = torch.cat([x1, x2, x3], dim=1)
        v1 = v0[:, 0:9223372036854775807]
        v2 = v1[:, 0:self.size1]
        v3 = torch.zeros([v2.shape[0], ((v2.shape[1] + v0.shape[1]) - self.size1)], dtype=torch.float32)
        v3[:, 0:self.size1] = v2
        v4 = (v0 + v3)
        return v4



size1 = 1
size2 = 1

func = Model(size1, size2).to('cuda')



x1 = torch.randn(1, 1, 64, 64)



x2 = torch.randn(1, 1, 32, 32)



x3 = torch.randn(1, 1, 32, 32)


test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
Sizes of tensors must match except in dimension 1. Expected size 64 but got size 32 for tensor number 1 in the list.

jit:
Failed running call_function <built-in method cat of type object at 0x7f7eaee699e0>(*([FakeTensor(..., device='cuda:0', size=(1, 1, 64, 64)), FakeTensor(..., device='cuda:0', size=(1, 1, 32, 32)), FakeTensor(..., device='cuda:0', size=(1, 1, 32, 32))],), **{'dim': 1}):
Sizes of tensors must match except in dimension 1. Expected 64 but got 32 for tensor number 1 in the list

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''