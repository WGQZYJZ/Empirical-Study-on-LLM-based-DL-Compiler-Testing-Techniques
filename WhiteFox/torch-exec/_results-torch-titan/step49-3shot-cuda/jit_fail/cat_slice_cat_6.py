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
        v1 = torch.cat([x1, x2, x3], dim=1)
        v2 = v1[:, 0:9223372036854775807]
        v3 = v2[:, 0:1]
        v4 = torch.cat([v1, v3], dim=1)
        v5 = torch.cat([x4, x5, x6], dim=1)
        v6 = v5[:, 0:1]
        v7 = torch.cat([v5, v6], dim=1)
        v8 = torch.cat([v4, v7], dim=1)
        return v8



func = Model().to('cuda')



x1 = torch.randn(1, 64, 148, 53)



x2 = torch.randn(1, 64, 74, 26)



x3 = torch.randn(1, 64, 37, 13)



x4 = torch.randn(1, 64, 64, 32)



x5 = torch.randn(1, 64, 32, 16)



x6 = torch.randn(1, 64, 16, 8)


test_inputs = [x1, x2, x3, x4, x5, x6]

# JIT_FAIL
'''
direct:
Sizes of tensors must match except in dimension 1. Expected size 148 but got size 74 for tensor number 1 in the list.

jit:
Failed running call_function <built-in method cat of type object at 0x702058a699e0>(*([FakeTensor(..., device='cuda:0', size=(1, 64, 148, 53)), FakeTensor(..., device='cuda:0', size=(1, 64, 74, 26)), FakeTensor(..., device='cuda:0', size=(1, 64, 37, 13))],), **{'dim': 1}):
Sizes of tensors must match except in dimension 1. Expected 148 but got 74 for tensor number 1 in the list

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''