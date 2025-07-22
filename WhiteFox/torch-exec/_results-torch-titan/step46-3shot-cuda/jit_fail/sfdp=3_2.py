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

    def forward(self, query, key, value, scale_factor, dropout_p):
        v1 = torch.matmul(query, key.transpose((- 2), (- 1)))
        v2 = v1.mul(scale_factor)
        v3 = v2.softmax(dim=(- 1))
        v4 = torch.nn.functional.dropout(v3, p=dropout_p)
        v5 = torch.matmul(dropout_q, value)
        return v5



func = Model().to('cuda')



query = torch.randn(8, 3, 32, 5)



key = torch.randn(8, 6, 32, 10)



value = torch.randn(8, 6, 32, 10)




scale_factor = torch.tensor([0.0], dtype=torch.float)




dropout_p = torch.tensor([0.1], dtype=torch.float)


test_inputs = [query, key, value, scale_factor, dropout_p]

# JIT_FAIL
'''
direct:
The size of tensor a (3) must match the size of tensor b (6) at non-singleton dimension 1

jit:
Failed running call_function <built-in method matmul of type object at 0x72fb154699e0>(*(FakeTensor(..., device='cuda:0', size=(8, 3, 32, 5)), FakeTensor(..., device='cuda:0', size=(8, 6, 10, 32))), **{}):
Shape mismatch: objects cannot be broadcast to a single shape

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''