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
        t1 = torch.cat([x1, x2, x3], dim=1)
        t2 = t1[:, 0:9223372036854775807]
        t3 = t2[:, 0:len(x1[0])]
        t4 = torch.cat([t1, t3], dim=1)
        return t4



func = Model().to('cuda')



x1 = torch.randn(1, 64, 43, 43)



x2 = torch.randn(1, 64, 16, 16)



x3 = torch.randn(1, 64, 32, 32)


test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
Sizes of tensors must match except in dimension 1. Expected size 43 but got size 16 for tensor number 1 in the list.

jit:
Failed running call_function <built-in method cat of type object at 0x77a4f30699e0>(*([FakeTensor(..., device='cuda:0', size=(1, 64, 43, 43)), FakeTensor(..., device='cuda:0', size=(1, 64, 16, 16)), FakeTensor(..., device='cuda:0', size=(1, 64, 32, 32))],), **{'dim': 1}):
Sizes of tensors must match except in dimension 1. Expected 43 but got 16 for tensor number 1 in the list

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''