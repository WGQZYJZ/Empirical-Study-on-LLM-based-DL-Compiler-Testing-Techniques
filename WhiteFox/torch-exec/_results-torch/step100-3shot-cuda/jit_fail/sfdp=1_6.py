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

class Model1(torch.nn.Module):

    def __init__(self):
        super().__init__()

    def forward(self, query, key, value, inv_scale_factor, dropout_p):
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output


func = Model1().to('cuda')


query = torch.randn(4, 8, 4, 4)

key = torch.randn(4, 16, 2, 2)

value = torch.randn(4, 16, 2, 2)

inv_scale_factor = torch.randn(16)

dropout_p = torch.tensor(0.1)

test_inputs = [query, key, value, inv_scale_factor, dropout_p]

# JIT_FAIL
'''
direct:
The size of tensor a (8) must match the size of tensor b (16) at non-singleton dimension 1

jit:
Failed running call_function <built-in method matmul of type object at 0x787ba2396ec0>(*(FakeTensor(..., device='cuda:0', size=(s4, s5, s6, s7)), FakeTensor(..., device='cuda:0', size=(s0, s1, s3, s2))), **{}):
Shape mismatch: objects cannot be broadcast to a single shape

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''