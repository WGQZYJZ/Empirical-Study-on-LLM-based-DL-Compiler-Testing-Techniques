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

    def forward(self, *x):
        v1 = x[0]
        for t in x[1:]:
            v1 = torch.cat([v1, t], dim=1)
        v2 = torch.squeeze(v1)
        v3 = v2[:, 0:self.size]
        v4 = torch.cat([v1, v3], dim=1)
        return v4



size = 1
func = Model(10).to('cuda')



x1 = torch.randn(1, 2, 10)



x2 = torch.randn(1, 1, 10)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Tensors must have same number of dimensions: got 3 and 2

jit:
Failed running call_function <built-in method cat of type object at 0x743fabc699e0>(*([FakeTensor(..., device='cuda:0', size=(1, 3, 10)), FakeTensor(..., device='cuda:0', size=(3, 10))],), **{'dim': 1}):
Sizes of tensors must match except in dimension 1. Expected 1 but got 3 for tensor number 1 in the list

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''