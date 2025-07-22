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

    def forward(self, query, key, value, inv_scale_factor, dropout_p):
        v1 = torch.matmul(query, key.transpose(-2, -1))
        v2 = v1.div(inv_scale_factor)
        v3 = v2.softmax(dim=-1)
        v4 = torch.nn.functional.dropout(v3, p=dropout_p)
        v5 = v4.matmul(value)
        return v5


func = Model().to('cpu')


query = torch.randn(1, 8, 137, 20)

key = torch.randn(1, 8, 56, 34)

value = torch.randn(1, 8, 56, 34)

inv_scale_factor = torch.rand(1)

dropout_p = torch.rand(1)

test_inputs = [query, key, value, inv_scale_factor, dropout_p]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [8, 20] but got: [8, 34].

jit:
Failed running call_function <built-in method matmul of type object at 0x7d2ce0d96ec0>(*(FakeTensor(..., size=(1, 8, 137, 20)), FakeTensor(..., size=(1, 8, 34, 56))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [8, 20] but got: [8, 34].

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''