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

    def forward(self, query, key, value):
        Q = query
        K = key
        V = value
        A = (Q @ K.T)
        inv_scale = (1.0 / math.sqrt(d_k))
        A = (A * inv_scale)
        A = torch.softmax(A, dim=(- 1))
        B = (A @ V)
        output = torch.nn.functional.dropout(B, p=dropout, training=self.training)
        return output



func = Model().to('cuda')



query = torch.randn(2, 3, 64)



key = torch.randn(2, 3, 64)



value = torch.randn(2, 3, 64)


test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
The size of tensor a (2) must match the size of tensor b (64) at non-singleton dimension 0

jit:
Failed running call_function <built-in function matmul>(*(FakeTensor(..., device='cuda:0', size=(2, 3, 64)), FakeTensor(..., device='cuda:0', size=(64, 3, 2))), **{}):
Shape mismatch: objects cannot be broadcast to a single shape

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''