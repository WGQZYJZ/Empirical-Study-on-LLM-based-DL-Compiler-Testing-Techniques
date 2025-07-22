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

    def forward(self, x1, x2, x3, x4, x5):
        v1 = torch.cat([x1, x2, x3, x4, x5], dim=1)
        v2 = v1[:, 0:9223372036854775807]
        v3 = v2[:, 0:v3.size(3)]
        v4 = torch.cat([v1, v3], dim=1)
        return v4



func = Model().to('cuda')



x1 = torch.randn(1, 1, 250, 50)



x2 = torch.randn(1, 1, 250, 80)



x3 = torch.randn(1, 1, 250, 90)



x4 = torch.randn(1, 1, 250, 5)



x5 = torch.randn(1, 1, 250, 20)


test_inputs = [x1, x2, x3, x4, x5]

# JIT_FAIL
'''
direct:
Sizes of tensors must match except in dimension 1. Expected size 50 but got size 80 for tensor number 1 in the list.

jit:
Failed running call_function <built-in method cat of type object at 0x7c24640699e0>(*([FakeTensor(..., device='cuda:0', size=(1, 1, 250, 50)), FakeTensor(..., device='cuda:0', size=(1, 1, 250, 80)), FakeTensor(..., device='cuda:0', size=(1, 1, 250, 90)), FakeTensor(..., device='cuda:0', size=(1, 1, 250, 5)), FakeTensor(..., device='cuda:0', size=(1, 1, 250, 20))],), **{'dim': 1}):
Sizes of tensors must match except in dimension 1. Expected 50 but got 80 for tensor number 1 in the list

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''