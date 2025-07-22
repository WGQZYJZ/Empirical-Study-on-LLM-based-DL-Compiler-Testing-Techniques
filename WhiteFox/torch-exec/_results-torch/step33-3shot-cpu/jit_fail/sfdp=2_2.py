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

    def __init__(self, d_model, d_qk, scale_factor, dropout_p):
        super().__init__()
        self.qk = torch.nn.Linear(d_model, d_qk)
        self.scaled_qk = torch.nn.Linear(d_qk, 1)
        self.inv_scale_factor = 1 / scale_factor
        self.dropout_p = dropout_p

    def forward(self, query, key, value):
        qk = self.qk(query)
        scaled_qk = self.scaled_qk(qk).div(self.inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = dropout_qk.matmul(value)
        return output


d_model = 1
d_qk = 1
scale_factor = 1
dropout_p = 1
func = Model(128, 32, 10, 0.5).to('cpu')


query = torch.randn(5, 128)

key = torch.randn(6, 128)

value = torch.randn(6, 128)

test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (5x1 and 6x128)

jit:
Failed running call_method matmul(*(FakeTensor(..., size=(5, 1)), FakeTensor(..., size=(6, 128))), **{}):
a and b must have same reduction dim, but got [5, 1] X [6, 128].

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''