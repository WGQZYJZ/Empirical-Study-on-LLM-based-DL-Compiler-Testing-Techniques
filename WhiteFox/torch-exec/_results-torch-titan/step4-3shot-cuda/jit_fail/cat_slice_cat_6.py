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

    def forward(self, x1, x2, x3, x4, x5, x6, x7, x8):
        v1 = torch.cat((x1, x2))
        v2 = v1[:, ::2]
        v3 = torch.cat((v1, v2))
        v4 = v3[:, :(- 87648823)]
        v5 = torch.cat((v4, v2, v3))
        return v5



func = Model().to('cuda')



x1 = torch.randn(1, 8, 64, 64)



x2 = torch.randn(1, 16, 64, 64)



x3 = torch.randn(1, 32, 64, 64)



x4 = torch.randn(1, 64, 64, 64)



x5 = torch.randn(1, 128, 64, 64)



x6 = torch.randn(1, 256, 64, 64)



x7 = torch.randn(1, 256, 64, 64)



x8 = torch.randn(1, 512, 64, 64)


test_inputs = [x1, x2, x3, x4, x5, x6, x7, x8]

# JIT_FAIL
'''
direct:
Sizes of tensors must match except in dimension 0. Expected size 8 but got size 16 for tensor number 1 in the list.

jit:
Failed running call_function <built-in method cat of type object at 0x761577c699e0>(*((FakeTensor(..., device='cuda:0', size=(1, 8, 64, 64)), FakeTensor(..., device='cuda:0', size=(1, 16, 64, 64))),), **{}):
Sizes of tensors must match except in dimension 0. Expected 8 but got 16 for tensor number 1 in the list

from user code:
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''