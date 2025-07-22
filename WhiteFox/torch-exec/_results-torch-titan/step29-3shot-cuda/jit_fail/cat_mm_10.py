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

    def forward(self, x, y, z):
        v1 = torch.mm(x, y)
        v2 = torch.mm(x, z)
        v3 = torch.mm(y, z)
        return torch.cat([v1, v2, v3, v3, v2], 1)




func = Model().to('cuda')



x = torch.randn(3, 2)



y = torch.randn(2, 2)



z = torch.randn(2, 2)


test_inputs = [x, y, z]

# JIT_FAIL
'''
direct:
Sizes of tensors must match except in dimension 1. Expected size 3 but got size 2 for tensor number 2 in the list.

jit:
Failed running call_function <built-in method cat of type object at 0x72a01fc699e0>(*([FakeTensor(..., device='cuda:0', size=(3, 2)), FakeTensor(..., device='cuda:0', size=(3, 2)), FakeTensor(..., device='cuda:0', size=(2, 2)), FakeTensor(..., device='cuda:0', size=(2, 2)), FakeTensor(..., device='cuda:0', size=(3, 2))], 1), **{}):
Sizes of tensors must match except in dimension 1. Expected 3 but got 2 for tensor number 2 in the list

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''