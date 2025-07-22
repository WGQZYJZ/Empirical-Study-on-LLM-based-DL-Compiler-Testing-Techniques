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
        self.linear = torch.nn.Linear(64, 16)
        self.sigmoid = torch.nn.Sigmoid()

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.relu(v1)
        v3 = self.sigmoid(v1)
        v4 = torch.tanh(v1)
        v5 = torch.softmax(v1)
        v6 = torch.sigmoid(v1)
        return (v2, v3, v4, v5, v6)



func = Model().to('cuda')



x1 = torch.randn(1, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
softmax() received an invalid combination of arguments - got (Tensor), but expected one of:
 * (Tensor input, int dim, torch.dtype dtype, *, Tensor out)
 * (Tensor input, name dim, *, torch.dtype dtype)


jit:
Failed running call_function <built-in method softmax of type object at 0x7c7f28c699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 16)),), **{}):
softmax() received an invalid combination of arguments - got (FakeTensor), but expected one of:
 * (Tensor input, int dim, torch.dtype dtype, *, Tensor out)
 * (Tensor input, name dim, *, torch.dtype dtype)


from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''