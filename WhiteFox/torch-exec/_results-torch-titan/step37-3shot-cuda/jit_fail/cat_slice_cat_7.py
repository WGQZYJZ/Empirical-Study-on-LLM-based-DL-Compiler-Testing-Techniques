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

    def forward(self, x1, x2):
        v1 = torch.cat([x1, x2], dim=1)
        v2 = v1[:, 0:9223372036854775807]
        v3 = v2[:, 0:63]
        v4 = torch.cat([v1, v3], dim=1)
        return v4



func = Model().to('cuda')



x1 = torch.randn(1, 64, 101, 101)



x2 = torch.randn(1, 64, 100, 100)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Sizes of tensors must match except in dimension 1. Expected size 101 but got size 100 for tensor number 1 in the list.

jit:
Failed running call_function <built-in method cat of type object at 0x703cc16699e0>(*([FakeTensor(..., device='cuda:0', size=(1, 64, 101, 101)), FakeTensor(..., device='cuda:0', size=(1, 64, 100, 100))],), **{'dim': 1}):
Sizes of tensors must match except in dimension 1. Expected 101 but got 100 for tensor number 1 in the list

from user code:
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''