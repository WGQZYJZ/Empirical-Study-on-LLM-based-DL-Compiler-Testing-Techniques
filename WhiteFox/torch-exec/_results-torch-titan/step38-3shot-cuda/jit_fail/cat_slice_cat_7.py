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

    def forward(self, x1, x2, x3, x4, size):
        t1 = torch.cat([x3, x1])
        t2 = t1[:, :size]
        t3 = torch.cat([t1, t2], dim=1)
        return t3



func = Model().to('cuda')



x1 = torch.randn(1, 64)



x2 = torch.randn(1, 32)



x3 = torch.randn(1, 16)



x4 = torch.randn(1, 8)

size = 1

test_inputs = [x1, x2, x3, x4, size]

# JIT_FAIL
'''
direct:
Sizes of tensors must match except in dimension 0. Expected size 16 but got size 64 for tensor number 1 in the list.

jit:
Failed running call_function <built-in method cat of type object at 0x7a29dd0699e0>(*([FakeTensor(..., device='cuda:0', size=(1, 16)), FakeTensor(..., device='cuda:0', size=(1, 64))],), **{}):
Sizes of tensors must match except in dimension 0. Expected 16 but got 64 for tensor number 1 in the list

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''