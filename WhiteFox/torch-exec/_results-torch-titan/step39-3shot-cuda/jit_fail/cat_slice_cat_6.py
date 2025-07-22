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

    def forward(self, x1, x2, x3):
        c1 = torch.cat((x1, x2, x3), dim=1)
        c2 = c1[:, 0:18446744073709551615]
        c3 = c2[:, 0:68]
        c4 = torch.cat([c1, c3], dim=1)
        return c1



func = Model().to('cuda')



x1 = torch.randn(1, 3, 128, 128)



x2 = torch.randn(1, 3, 64, 64)



x3 = torch.randn(1, 3, 32, 32)


test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
Sizes of tensors must match except in dimension 1. Expected size 128 but got size 64 for tensor number 1 in the list.

jit:
Failed running call_function <built-in method cat of type object at 0x7b3f000699e0>(*((FakeTensor(..., device='cuda:0', size=(1, 3, 128, 128)), FakeTensor(..., device='cuda:0', size=(1, 3, 64, 64)), FakeTensor(..., device='cuda:0', size=(1, 3, 32, 32))),), **{'dim': 1}):
Sizes of tensors must match except in dimension 1. Expected 128 but got 64 for tensor number 1 in the list

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''