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
        self.c1 = torch.nn.Conv2d(2, 2, 2)

    def forward(self, x1):
        z1 = torch.nn.functional.dropout(self.c1(x1), p=0.5)
        z2 = torch.rand_like(self.c1(x1), dtype=torch.float)
        z1 = torch.nn.functional.dropout(torch.log_softmax(torch.nn.functional.elu(z2.abs())), p=0.3)
        return z1




func = Model().to('cuda')



x1 = torch.randn(2, 2, 5, 5)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
log_softmax() received an invalid combination of arguments - got (Tensor), but expected one of:
 * (Tensor input, int dim, torch.dtype dtype, *, Tensor out)
 * (Tensor input, name dim, *, torch.dtype dtype)


jit:
Failed running call_function <built-in method log_softmax of type object at 0x72bc38a699e0>(*(FakeTensor(..., device='cuda:0', size=(2, 2, 4, 4)),), **{}):
log_softmax() received an invalid combination of arguments - got (FakeTensor), but expected one of:
 * (Tensor input, int dim, torch.dtype dtype, *, Tensor out)
 * (Tensor input, name dim, *, torch.dtype dtype)


from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''