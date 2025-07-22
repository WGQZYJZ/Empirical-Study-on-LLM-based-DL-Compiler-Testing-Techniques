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

    def __init__(self, size):
        super().__init__()
        self.size = size

    def forward(self, x1, x2, x3, x4, x5):
        v1 = torch.cat([x1, x2, x3, x4, x5], dim=1)
        v2 = v1[:, 0:9223372036854775807]
        v3 = v2[:, 0:self.size]
        v4 = torch.cat([v1, v3], dim=1)
        return v4




size = 2

func = Model(size).to('cuda')



x1 = torch.randn(1, 1, 2, 3, 4)



x2 = torch.randn(1, 2, 3, 4)



x3 = torch.randn(1, 3, 2, 3)



x4 = torch.randn(1, 4, 3)



x5 = torch.randn(1, 5)


test_inputs = [x1, x2, x3, x4, x5]

# JIT_FAIL
'''
direct:
Tensors must have same number of dimensions: got 5 and 4

jit:
Failed running call_function <built-in method cat of type object at 0x79873ac699e0>(*([FakeTensor(..., device='cuda:0', size=(1, 1, 2, 3, 4)), FakeTensor(..., device='cuda:0', size=(1, 2, 3, 4)), FakeTensor(..., device='cuda:0', size=(1, 3, 2, 3)), FakeTensor(..., device='cuda:0', size=(1, 4, 3)), FakeTensor(..., device='cuda:0', size=(1, 5))],), **{'dim': 1}):
Sizes of tensors must match except in dimension 1. Expected 2 but got 3 for tensor number 1 in the list

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''