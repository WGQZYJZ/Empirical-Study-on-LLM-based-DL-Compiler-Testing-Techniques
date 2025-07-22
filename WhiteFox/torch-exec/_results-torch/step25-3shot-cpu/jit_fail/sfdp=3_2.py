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

    def __init__(self, num_heads, query_size, key_size, value_size, input_size):
        super().__init__()
        self.query = torch.nn.Linear(query_size, num_heads * key_size)
        self.key = torch.nn.Linear(key_size, num_heads * key_size)
        self.value = torch.nn.Linear(value_size, num_heads * value_size)
        self.output = torch.nn.Linear(num_heads * value_size, input_size)
        self.dropout_p = 0.75
        self.scale_factor = 1 / query_size ** 0.5

    def forward(self, x1, x2, x3):
        query = self.query(x1)
        key = self.key(x2)
        value = self.value(x3)
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk.mul(self.scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = self.output(dropout_qk.matmul(value))
        return output


num_heads = 1
query_size = 1
key_size = 1
value_size = 1
input_size = 1

func = Model(num_heads, query_size, key_size, value_size, input_size).to('cpu')


x1 = torch.randn(1, 8, 32)

x2 = torch.randn(1, 8, 32)

x3 = torch.randn(1, 8, 32)

test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (8x32 and 1x1)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 8, 32)), Parameter(FakeTensor(..., size=(1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(1,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [8, 32] X [1, 1].

from user code:
   File "<string>", line 25, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''