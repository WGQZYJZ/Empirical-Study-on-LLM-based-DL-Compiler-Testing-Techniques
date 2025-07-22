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

    def forward(self, a1, a2):
        v1 = torch.cat([a1, a2], dim=1)
        v2 = v1[:, :, :, 0:9223372036854775807]
        v3 = v2[:, :, :, 0:10]
        v4 = torch.cat([v1, v3], dim=1)
        return v4



func = Model().to('cuda')



a1 = torch.randn(1, 3, 60, 10)



a2 = torch.randn(1, 3, 50, 10)


test_inputs = [a1, a2]

# JIT_FAIL
'''
direct:
Sizes of tensors must match except in dimension 1. Expected size 60 but got size 50 for tensor number 1 in the list.

jit:
Failed running call_function <built-in method cat of type object at 0x702a97a699e0>(*([FakeTensor(..., device='cuda:0', size=(1, 3, 60, 10)), FakeTensor(..., device='cuda:0', size=(1, 3, 50, 10))],), **{'dim': 1}):
Sizes of tensors must match except in dimension 1. Expected 60 but got 50 for tensor number 1 in the list

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''