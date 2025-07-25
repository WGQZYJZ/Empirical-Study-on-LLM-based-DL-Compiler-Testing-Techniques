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

    def __init__(self, dim, num_heads, dim_out):
        super().__init__()
        self.num_heads = num_heads
        self.wq = torch.nn.Linear(dim, dim, bias=False)
        self.wk = torch.nn.Linear(dim, dim, bias=False)
        self.wv = torch.nn.Linear(dim, dim, bias=False)
        self.wo = torch.nn.Linear(dim, dim_out, bias=False)
        self.scale_factor = math.sqrt(dim_out / self.num_heads)
        self.dropout_p = 0.2

    def forward(self, x1, x2):
        batch_size = x1.shape[0]
        query = self.wq(x1)
        key = self.wk(x2)
        value = self.wv(x2)
        flat_query = query.view((batch_size * self.num_heads, -1, query.shape[-1]))
        flat_key = key.view((batch_size * self.num_heads, -1, key.shape[-1]))
        flat_value = value.view((batch_size * self.num_heads, -1, value.shape[-1]))
        flat_scaled_qk = torch.matmul(flat_query, flat_key.transpose(1, 2)) * self.scale_factor
        flat_softmax_qk = flat_scaled_qk.softmax(dim=-1)
        flat_dropout_qk = torch.nn.functional.dropout(flat_softmax_qk, p=self.dropout_p)
        output = flat_dropout_qk.matmul(flat_value)
        output = output.view((batch_size, -1, output.shape[-1])).transpose(1, 2)
        return self.wo(output)


dim = 1
num_heads = 1
dim_out = 1

func = Model(dim, num_heads, dim_out).to('cpu')


x1 = torch.randn(1, 5, 20)
x2 = 1

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (5x20 and 1x1)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 5, 20)), Parameter(FakeTensor(..., size=(1, 1), requires_grad=True)), None), **{}):
a and b must have same reduction dim, but got [5, 20] X [1, 1].

from user code:
   File "<string>", line 27, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''