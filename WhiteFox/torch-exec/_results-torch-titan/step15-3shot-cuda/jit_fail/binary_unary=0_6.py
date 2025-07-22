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
        self.conv = torch.nn.Linear(128, 128)

    def forward(self, x):
        v1 = self.conv(x)
        v2 = torch.softmax(v1)
        v3 = (v2 + x)
        return v3




func = Model().to('cuda')



x = torch.randn(1, 128)


test_inputs = [x]

# JIT_FAIL
'''
direct:
softmax() received an invalid combination of arguments - got (Tensor), but expected one of:
 * (Tensor input, int dim, torch.dtype dtype, *, Tensor out)
 * (Tensor input, name dim, *, torch.dtype dtype)


jit:
Failed running call_function <built-in method softmax of type object at 0x79300fe699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 128)),), **{}):
softmax() received an invalid combination of arguments - got (FakeTensor), but expected one of:
 * (Tensor input, int dim, torch.dtype dtype, *, Tensor out)
 * (Tensor input, name dim, *, torch.dtype dtype)


from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''