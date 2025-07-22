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

    def forward(self, x):
        x1 = torch.transpose(x, 1, 2)
        x2 = torch.transpose(x, 1, 3)
        x3 = torch.cat([x1, x2], dim=1)
        x4 = x3[:, :, :, 0:9223372036854775807]
        x5 = x4[:, :, :, 0:494967295]
        x6 = torch.cat([x3, x5], dim=3)
        x7 = torch.transpose(x6, 1, 2)
        x8 = torch.transpose(x7, 1, 3)
        return x8



func = Model().to('cuda')



x = torch.randn(4, 64, 1, 1792)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Sizes of tensors must match except in dimension 1. Expected size 64 but got size 1 for tensor number 1 in the list.

jit:
Failed running call_function <built-in method cat of type object at 0x77a4f30699e0>(*([FakeTensor(..., device='cuda:0', size=(4, 1, 64, 1792)), FakeTensor(..., device='cuda:0', size=(4, 1792, 1, 64))],), **{'dim': 1}):
Sizes of tensors must match except in dimension 1. Expected 64 but got 1 for tensor number 1 in the list

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''