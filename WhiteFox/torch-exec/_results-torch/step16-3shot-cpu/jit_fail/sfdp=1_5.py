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

    def __init__(self, num_q, num_k, num_v, dropout_p, inv_scale_factor):
        super().__init__()
        self.w = torch.nn.Linear(num_q, num_v)
        self.x = torch.nn.Linear(num_k, num_v)
        self.dropout_p = dropout_p
        self.inv_scale_factor = inv_scale_factor

    def forward(self, query1, key1, value1):
        q = self.w(query1)
        k = self.x(key1)
        qk = torch.matmul(q, k.transpose(-2, -1))
        scaled_qk = qk.div(self.inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        v = value1
        output = dropout_qk.matmul(v)
        return output


num_q = 1
num_k = 1
num_v = 1
dropout_p = 1
inv_scale_factor = 1
func = Model(2, 3, 4, 0.5, 0.1).to('cpu')


query1 = torch.randn(1, 2, 1)

key1 = torch.randn(1, 3, 1)

value1 = torch.randn(1, 4, 1)

test_inputs = [query1, key1, value1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (2x1 and 2x4)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 2, 1)), Parameter(FakeTensor(..., size=(4, 2), requires_grad=True)), Parameter(FakeTensor(..., size=(4,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [2, 1] X [2, 4].

from user code:
   File "<string>", line 23, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''