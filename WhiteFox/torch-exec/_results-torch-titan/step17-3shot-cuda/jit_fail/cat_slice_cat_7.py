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

    def forward(self, x1, x2, x3):
        t1 = torch.cat([x1, x2, x3], dim=1)
        t2 = t1[:, 0:9223372036854775807]
        t3 = t2[:, 0:17]
        t4 = torch.cat([t1, t3], dim=1)
        return t4



func = Model().to('cuda')



x1 = torch.randn(1, 1, 128, 128)



x2 = torch.randn(1, 196608, 1, 1)



x3 = torch.randn(1, 2048, 1, 1)


test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
Sizes of tensors must match except in dimension 1. Expected size 128 but got size 1 for tensor number 1 in the list.

jit:
Failed running call_function <built-in method cat of type object at 0x75e02f4699e0>(*([FakeTensor(..., device='cuda:0', size=(1, 1, 128, 128)), FakeTensor(..., device='cuda:0', size=(1, 196608, 1, 1)), FakeTensor(..., device='cuda:0', size=(1, 2048, 1, 1))],), **{'dim': 1}):
Sizes of tensors must match except in dimension 1. Expected 128 but got 1 for tensor number 1 in the list

from user code:
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''