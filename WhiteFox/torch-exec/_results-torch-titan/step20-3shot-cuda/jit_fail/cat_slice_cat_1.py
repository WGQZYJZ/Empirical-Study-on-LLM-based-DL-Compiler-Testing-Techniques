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

    def forward(self, x, y, z):
        v = torch.cat([x, y, z], dim=1)
        v1 = v[:, 0:9223372036854775807]
        v2 = v1[:, 0:v2.shape[1]]
        v3 = torch.cat([v, v2], dim=1)
        return v3



func = Model().to('cuda')



x = torch.randn(1, 3, 5)



y = torch.randn(1, 3, 11)



z = torch.randn(1, 3, 25)


test_inputs = [x, y, z]

# JIT_FAIL
'''
direct:
Sizes of tensors must match except in dimension 1. Expected size 5 but got size 11 for tensor number 1 in the list.

jit:
Failed running call_function <built-in method cat of type object at 0x73f6cfa699e0>(*([FakeTensor(..., device='cuda:0', size=(1, 3, 5)), FakeTensor(..., device='cuda:0', size=(1, 3, 11)), FakeTensor(..., device='cuda:0', size=(1, 3, 25))],), **{'dim': 1}):
Sizes of tensors must match except in dimension 1. Expected 5 but got 11 for tensor number 1 in the list

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''