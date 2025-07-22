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
        v1 = torch.sum(x1, [2, 3])
        v2 = torch.softmax(v1)
        return v2




func = Model().to('cuda')



x1 = torch.randn(1, 1, 3, 3)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
softmax() received an invalid combination of arguments - got (Tensor), but expected one of:
 * (Tensor input, int dim, torch.dtype dtype, *, Tensor out)
 * (Tensor input, name dim, *, torch.dtype dtype)


jit:
Failed running call_function <built-in method softmax of type object at 0x70673dc699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 1)),), **{}):
softmax() received an invalid combination of arguments - got (FakeTensor), but expected one of:
 * (Tensor input, int dim, torch.dtype dtype, *, Tensor out)
 * (Tensor input, name dim, *, torch.dtype dtype)


from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''