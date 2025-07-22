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

    def __init__(self, query_dim, key_dim, nheads, dropout_p):
        super().__init__()
        self.query_dim = query_dim
        self.key_dim = key_dim
        self.nheads = nheads
        self.dropout_p = dropout_p

    def forward(self, query, key, value, inv_scale_factor):
        _ = query.size()
        _ = key.size()
        _ = value.size()
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = dropout_qk.matmul(value)
        return output



query_dim = 1
key_dim = 1
nheads = 1
dropout_p = 1

func = Model(query_dim, key_dim, nheads, dropout_p).to('cuda')



x1 = torch.randn(1, 3, 64, 64)



x2 = torch.randn(1, 32, 64, 64)



x3 = torch.randn(1, 32, 128, 128)

query = 1

test_inputs = [x1, x2, x3, query]

# JIT_FAIL
'''
direct:
The size of tensor a (3) must match the size of tensor b (32) at non-singleton dimension 1

jit:
Failed running call_function <built-in method matmul of type object at 0x765219c699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 3, 64, 64)), FakeTensor(..., device='cuda:0', size=(1, 32, 64, 64))), **{}):
Shape mismatch: objects cannot be broadcast to a single shape

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''