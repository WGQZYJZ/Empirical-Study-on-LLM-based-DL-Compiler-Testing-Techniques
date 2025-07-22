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

    def forward(self, x0, x2):
        v0 = x0.permute(0, 2, 1)
        v1 = x0.permute(0, 2, 1)
        v2 = x2.permute(0, 2, 1)
        v3 = x2.permute(0, 2, 1)
        v4 = x0.permute(0, 2, 1)
        v5 = torch.matmul(v2, v1)
        v6 = torch.matmul(v1, v0)
        v7 = torch.matmul(v5, v4)
        r2 = torch.randn(1, 3, 3)
        v11 = torch.cat((v7, r2), dim=1)
        return torch.tanh(v11)




func = Model().to('cuda')



x0 = torch.randn(1, 2, 2)



x2 = torch.randn(1, 2, 2)


test_inputs = [x0, x2]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu! (when checking argument for argument tensors in method wrapper_CUDA_cat)

jit:
Failed running call_function <built-in method cat of type object at 0x7ed5138699e0>(*((FakeTensor(..., device='cuda:0', size=(1, 2, 2)), FakeTensor(..., size=(1, 3, 3))),), **{'dim': 1}):
Sizes of tensors must match except in dimension 1. Expected 2 but got 3 for tensor number 1 in the list

from user code:
   File "<string>", line 30, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''