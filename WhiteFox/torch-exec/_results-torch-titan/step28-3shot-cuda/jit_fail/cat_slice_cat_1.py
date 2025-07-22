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

    def forward(self, x1, x2, size):
        x3 = torch.cat(x1, dim=1)
        x4 = x3[:, 0:9223372036854775807]
        x5 = x4[:, 0:size]
        return torch.cat([x3, x5], dim=1)



func = Model().to('cuda')



x1 = torch.randn(1, 16, 64, 64)



x2 = torch.randn(1, 8, 64, 64)

size = 1

test_inputs = [x1, x2, size]

# JIT_FAIL
'''
direct:
cat() received an invalid combination of arguments - got (Tensor, dim=int), but expected one of:
 * (tuple of Tensors tensors, int dim, *, Tensor out)
 * (tuple of Tensors tensors, name dim, *, Tensor out)


jit:
Failed running call_function <built-in method cat of type object at 0x7f7eaee699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 16, 64, 64)),), **{'dim': 1}):
cat() received an invalid combination of arguments - got (FakeTensor, dim=int), but expected one of:
 * (tuple of Tensors tensors, int dim, *, Tensor out)
 * (tuple of Tensors tensors, name dim, *, Tensor out)


from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''