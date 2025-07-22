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
        self.shape = [2, 3, 4, 5]

    def forward(self, x1, x2):
        v1 = torch.cat([x1, x2], dim=1)
        v2 = v1[:, 0:9223372036854775807]
        if (self.shape[3] != v2.shape[1]):
            x3 = torch.full(v1.shape, 12.0, dtype=torch.float32)
            v3 = torch.cat([v1, x3], dim=1)
            v4 = v3[:, 0:self.shape[3]]
        else:
            v4 = v2[:, 0:self.shape[3]]
        v5 = (v4 + 1)
        return v5



func = Model().to('cuda')



x1 = torch.randn(1, 3, 2, 2)



x2 = torch.randn(1, 3, 2, 5)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Sizes of tensors must match except in dimension 1. Expected size 2 but got size 5 for tensor number 1 in the list.

jit:
Failed running call_function <built-in method cat of type object at 0x7686ce4699e0>(*([FakeTensor(..., device='cuda:0', size=(1, 3, 2, 2)), FakeTensor(..., device='cuda:0', size=(1, 3, 2, 5))],), **{'dim': 1}):
Sizes of tensors must match except in dimension 1. Expected 2 but got 5 for tensor number 1 in the list

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''