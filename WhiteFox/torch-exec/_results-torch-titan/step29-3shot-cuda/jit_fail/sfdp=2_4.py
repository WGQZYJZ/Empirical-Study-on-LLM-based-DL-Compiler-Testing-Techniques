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

    def __init__(self, query_size, key_size, value_size):
        super().__init__()

    def forward(self, query, key, value, scale_factor, dropout_p):
        v1 = torch.matmul(query, key.transpose((- 2), (- 1)))
        v2 = v1.div(scale_factor)
        v3 = v2.softmax(dim=(- 1))
        v4 = torch.nn.functional().dropout(softmax_qk, p=dropout_p)
        v5 = torch.matmul(v4, value)
        return v5



query_size = 1
key_size = 1
value_size = 1
func = Model(10, 20, 30).to('cuda')



query = torch.randn(10, 20)



key = torch.randn(10, 30)



value = torch.randn(10, 30)

scale_factor = 1
dropout_p = 1

test_inputs = [query, key, value, scale_factor, dropout_p]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (10x20 and 30x10)

jit:
Failed running call_function <built-in method matmul of type object at 0x71703e2699e0>(*(FakeTensor(..., device='cuda:0', size=(10, 20)), FakeTensor(..., device='cuda:0', size=(30, 10))), **{}):
a and b must have same reduction dim, but got [10, 20] X [30, 10].

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''