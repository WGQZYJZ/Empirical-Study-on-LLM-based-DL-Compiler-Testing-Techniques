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
        self.linear = torch.nn.Linear(10, 20)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = (v1 * torch.clamp(torch.min(torch.max((v1 + 3), 0), 6), min=0, max=6))
        v3 = (v2 / 6)
        return v3



func = Model().to('cuda')



x1 = torch.randn(1, 10)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
min() received an invalid combination of arguments - got (torch.return_types.max, int), but expected one of:
 * (Tensor input, *, Tensor out)
 * (Tensor input, Tensor other, *, Tensor out)
 * (Tensor input, int dim, bool keepdim, *, tuple of Tensors out)
 * (Tensor input, name dim, bool keepdim, *, tuple of Tensors out)


jit:
Failed running call_function <built-in method min of type object at 0x725ff30699e0>(*((FakeTensor(..., device='cuda:0', size=(20,)), FakeTensor(..., device='cuda:0', size=(20,), dtype=torch.int64)), 6), **{}):
min() received an invalid combination of arguments - got (tuple, int), but expected one of:
 * (Tensor input, *, Tensor out)
 * (Tensor input, Tensor other, *, Tensor out)
 * (Tensor input, int dim, bool keepdim, *, tuple of Tensors out)
 * (Tensor input, name dim, bool keepdim, *, tuple of Tensors out)


from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''