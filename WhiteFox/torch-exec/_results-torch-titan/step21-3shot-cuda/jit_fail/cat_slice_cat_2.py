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

    def forward(self, x1, x2, x3, x4, x5):
        v1 = torch.cat([x1, x2], dim=1)
        v2 = v1[:, 0:(- 1)]
        v3 = v1[:, 0:int(v1.size(1))]
        v4 = torch.cat([v1, v3], dim=1)
        return (v4, v5, v6, v7, v8)



func = Model().to('cuda')



x1 = torch.randn(1, 100, 512)



x2 = torch.randn(1, 100, 768)



x3 = torch.randn(1, 100, 256)



x4 = torch.randn(1, 100, 64)



x5 = torch.randn(1, 100, 16)


test_inputs = [x1, x2, x3, x4, x5]

# JIT_FAIL
'''
direct:
Sizes of tensors must match except in dimension 1. Expected size 512 but got size 768 for tensor number 1 in the list.

jit:
Failed running call_function <built-in method cat of type object at 0x7ce4c52699e0>(*([FakeTensor(..., device='cuda:0', size=(1, 100, 512)), FakeTensor(..., device='cuda:0', size=(1, 100, 768))],), **{'dim': 1}):
Sizes of tensors must match except in dimension 1. Expected 512 but got 768 for tensor number 1 in the list

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''