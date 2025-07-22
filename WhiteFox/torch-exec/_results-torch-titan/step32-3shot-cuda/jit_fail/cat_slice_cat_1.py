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
        v1 = torch.cat([x1, x2, x3, x4], dim=1)
        v2 = v1[:, 0:9223372036854775807]
        v3 = v2[:, 0:size]
        v4 = torch.cat([v1, v3], dim=1)
        return v4



func = Model().to('cuda')



x1 = torch.randn(1, 3, 256, 256)



x2 = torch.randn(1, 3, 240, 240)



x3 = torch.randn(1, 3, 224, 224)



x4 = torch.randn(1, 3, 192, 192)



size = torch.randint(2, 10, (1,))


test_inputs = [x1, x2, x3, x4, size]

# JIT_FAIL
'''
direct:
Sizes of tensors must match except in dimension 1. Expected size 256 but got size 240 for tensor number 1 in the list.

jit:
Failed running call_function <built-in method cat of type object at 0x7bb51c4699e0>(*([FakeTensor(..., device='cuda:0', size=(1, 3, 256, 256)), FakeTensor(..., device='cuda:0', size=(1, 3, 240, 240)), FakeTensor(..., device='cuda:0', size=(1, 3, 224, 224)), FakeTensor(..., device='cuda:0', size=(1, 3, 192, 192))],), **{'dim': 1}):
Sizes of tensors must match except in dimension 1. Expected 256 but got 240 for tensor number 1 in the list

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''