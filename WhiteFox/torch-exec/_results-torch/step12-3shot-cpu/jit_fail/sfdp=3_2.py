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

    def __init__(self, in_features, num_heads, num_keys, key_size):
        super().__init__()
        self.query = torch.nn.Linear(in_features, key_size * num_heads)
        self.key = torch.nn.Linear(num_keys, key_size * num_heads)
        self.scale_factor = torch.sqrt(torch.Tensor([key_size]))
        self.dropout = torch.nn.Dropout(0.1)

    def forward(self, x1, x2):
        q = self.query(x1)
        q = q.reshape(q.shape[0], -1, q.shape[-1])
        k = self.key(x2)
        k = k.reshape(k.shape[0], -1, k.shape[-1])
        qk = torch.matmul(q, k.transpose(-1, -2))
        scaled_qk = qk * self.scale_factor
        softmax_qk = softmax(scaled_qk, dim=-1)
        dropout_qk = self.dropout(softmax_qk)
        output = torch.matmul(dropout_qk, v)
        output = output.reshape(-1, output.shape[-2] * output.shape[-1])
        return output


in_features = 1
num_heads = 1
num_keys = 1
key_size = 1
func = Model(10, 4, 120, 20).to('cpu')


x1 = torch.randn(4, 10)

x2 = torch.randn(15, 10)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (15x10 and 120x80)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(15, 10)), Parameter(FakeTensor(..., size=(80, 120), requires_grad=True)), Parameter(FakeTensor(..., size=(80,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [15, 10] X [120, 80].

from user code:
   File "<string>", line 25, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''