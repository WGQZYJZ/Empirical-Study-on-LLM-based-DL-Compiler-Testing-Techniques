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

    def __init__(self, query_size, key_size, value_size, scale_factor):
        super().__init__()
        self.dropout = torch.nn.Dropout()
        self.softmax_qk = torch.nn.Softmax(dim=-1)
        self.inv_scale_factor = 1.0 / float(scale_factor)

    def forward(self, query, key, value, dropout_p):
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk.div(self.inv_scale_factor)
        softmax_qk = self.softmax_qk(scaled_qk)
        dropout_qk = self.dropout(softmax_qk)
        output = dropout_qk.matmul(value)
        return output


query_size = 1
key_size = 1
value_size = 1
scale_factor = 1

func = Model(query_size, key_size, value_size, scale_factor).to('cpu')


query = torch.randn(2, 3)

key = torch.randn(2, 5)

value = torch.randn(2, 5)
dropout_p = 1

test_inputs = [query, key, value, dropout_p]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (2x3 and 5x2)

jit:
Failed running call_function <built-in method matmul of type object at 0x73e4f4996ec0>(*(FakeTensor(..., size=(2, 3)), FakeTensor(..., size=(5, 2))), **{}):
a and b must have same reduction dim, but got [2, 3] X [5, 2].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''