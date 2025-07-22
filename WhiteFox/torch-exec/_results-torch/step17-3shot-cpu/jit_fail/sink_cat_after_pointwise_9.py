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

    def forward(self, x0, x1):
        x2 = torch.cat((x0, x1), dim=1)
        x3 = x2.permute(0, 2, 1)
        x4 = x2.permute(0, 2, 1)
        x5 = torch.tanh(x3)
        x6 = torch.cat((x4, x5), dim=1)
        x7 = torch.relu(x5)
        y = torch.relu(x4)
        x8 = torch.tanh(x7)
        y = x6.view(x6.shape[0], x6.shape[1])
        y = y.permute(0, 2, 1)
        x9 = y.unsqueeze(dim=dim_size)
        x10 = torch.cat((x8, x9), dim=dim_size).view(x8.shape[0], x8.shape[1], x9.shape[2])
        x11 = x10.permute(0, 2, dim_size + 2, dim_size + 1)
        x12 = torch.tanh(x11)
        x13 = x12 + x11.type_as(x12)
        x14 = x13.view(-1, x13.size(dim_size + 1), x13.size(dim_size + 2))
        x15 = torch.relu(x14)
        x16 = x14 + x14.type_as(x13)
        x17 = x16.view(x16.shape[0], x16.shape[1], x16.shape[2])
        return x17



func = Model().to('cpu')


x0 = torch.randn(2, 3, 1, 5)

x1 = torch.zeros(2, 3, 1, 1)

test_inputs = [x0, x1]

# JIT_FAIL
'''
direct:
Sizes of tensors must match except in dimension 1. Expected size 5 but got size 1 for tensor number 1 in the list.

jit:
Failed running call_function <built-in method cat of type object at 0x7c4930b96ec0>(*((FakeTensor(..., size=(2, 3, 1, 5)), FakeTensor(..., size=(2, 3, 1, 1))),), **{'dim': 1}):
Sizes of tensors must match except in dimension 1. Expected 5 in dimension 3 but got 1 for tensor number 1 in the list

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''