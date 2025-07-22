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
        self.linear = torch.nn.Linear(3, 8)

    def forward(self, x):
        v1 = self.linear(x)
        v2 = (v1 * 0.5)
        v3 = torch.cat(v1.reshape((- 1)), v1.reshape((- 1))).unsqueeze(0)
        v4 = (v3 * 0.044715)
        v5 = (v4 * 0.7978845608028654)
        v6 = torch.tanh(v5)
        v7 = (v6 + 1)
        v8 = (v2 * v7)
        return v8



func = Model().to('cuda')



x = torch.randn(1, 3)


test_inputs = [x]

# JIT_FAIL
'''
direct:
cat() received an invalid combination of arguments - got (Tensor, Tensor), but expected one of:
 * (tuple of Tensors tensors, int dim, *, Tensor out)
 * (tuple of Tensors tensors, name dim, *, Tensor out)


jit:
Failed running call_function <built-in method cat of type object at 0x71d0128699e0>(*(FakeTensor(..., device='cuda:0', size=(8,)), FakeTensor(..., device='cuda:0', size=(8,))), **{}):
cat() received an invalid combination of arguments - got (FakeTensor, FakeTensor), but expected one of:
 * (tuple of Tensors tensors, int dim, *, Tensor out)
 * (tuple of Tensors tensors, name dim, *, Tensor out)


from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''