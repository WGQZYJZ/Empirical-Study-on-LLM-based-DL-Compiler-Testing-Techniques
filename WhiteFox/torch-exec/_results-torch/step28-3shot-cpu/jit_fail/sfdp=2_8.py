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
        self.q_linear = torch.nn.Linear(8, 8)
        self.k_linear = torch.nn.Linear(8, 8)
        self.k_t = None

    def forward(self, query, value, inv_scale_factor, dropout_p):
        query = self.q_linear(query)
        key = self.k_linear(value) if self.k_t is None else self.k_t(value)
        res = query.matmul(key.transpose(-2, -1))
        scaled_res = res.div(inv_scale_factor)
        softmax_res = torch.nn.functional.softmax(scaled_res, dim=-1)
        dropout_res = torch.nn.functional.dropout(softmax_res, p=dropout_p)
        output = dropout_res.matmul(value)
        return output


func = Model().to('cpu')


query = torch.randn(2, 8)

value = torch.randn(2, 8, 16)
inv_scale_factor = 1
dropout_p = 1

test_inputs = [query, value, inv_scale_factor, dropout_p]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (16x16 and 8x8)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(2, 8, 16)), Parameter(FakeTensor(..., size=(8, 8), requires_grad=True)), Parameter(FakeTensor(..., size=(8,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [16, 16] X [8, 8].

from user code:
   File "<string>", line 23, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''