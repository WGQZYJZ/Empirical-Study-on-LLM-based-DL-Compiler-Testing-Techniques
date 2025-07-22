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

    def forward(self, x1):
        v1 = torch.cat(x1, dim=1)
        v2 = v1[:, 0:2305843009213693950880000000000000000000000]
        v3 = v2[:, 0:10]
        v4 = torch.cat([v1, v3], dim=1)
        return v4



func = Model().to('cuda')

x1 = 1

test_inputs = [x1]

# JIT_FAIL
'''
direct:
cat() received an invalid combination of arguments - got (int, dim=int), but expected one of:
 * (tuple of Tensors tensors, int dim, *, Tensor out)
 * (tuple of Tensors tensors, name dim, *, Tensor out)


jit:
Failed running call_function <built-in method cat of type object at 0x702a97a699e0>(*(1,), **{'dim': 1}):
cat() received an invalid combination of arguments - got (int, dim=int), but expected one of:
 * (tuple of Tensors tensors, int dim, *, Tensor out)
 * (tuple of Tensors tensors, name dim, *, Tensor out)


from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''