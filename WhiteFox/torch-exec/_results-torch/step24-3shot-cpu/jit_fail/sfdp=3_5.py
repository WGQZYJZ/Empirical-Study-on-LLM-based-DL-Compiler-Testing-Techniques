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

    def __init__(self, input_dim, num_heads, num_features, dim_per_head=None):
        super().__init__()
        if not dim_per_head:
            self.dim_per_head = input_dim // num_heads
        else:
            self.dim_per_head = dim_per_head
        self.num_heads = num_heads
        self.linear_q = torch.nn.Linear(input_dim, self.dim_per_head * num_heads)
        self.linear_k = torch.nn.Linear(input_dim, self.dim_per_head * num_heads)
        self.linear_v = torch.nn.Linear(input_dim, self.dim_per_head * num_heads)
        self.linear_o = torch.nn.Linear(self.dim_per_head * num_heads, num_features)

    def forward(self, query, key, value, scale_factor=1.0, dropout_p=0):
        q = self.linear_q(query)
        k = self.linear_k(key)
        v = self.linear_v(value)
        qh = q.view(q.size(0), -1, self.num_heads, self.dim_per_head)
        kh = k.view(k.size(0), -1, self.num_heads, self.dim_per_head)
        vh = v.view(v.size(0), -1, self.num_heads, self.dim_per_head)
        scaled_dot_product = torch.sum(qh * kh.transpose(-2, -1), dim=-1) / scale_factor
        attn = torch.nn.functional.softmax(scaled_dot_product, dim=-1)
        attn = torch.nn.functional.dropout(attn, p=dropout_p)
        output = torch.matmul(attn, vh)
        output = output.view(output.size(0), -1, self.num_heads * output.size(-1))
        output = self.linear_o(output)
        return output


input_dim = 1
num_heads = 1
num_features = 1

func = Model(input_dim, num_heads, num_features).to('cpu')


query = torch.randn(1, 8, 64, 64)

key = torch.randn(1, 8, 64, 64)

value = torch.randn(1, 8, 64, 64)

test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (512x64 and 1x1)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 8, 64, 64)), Parameter(FakeTensor(..., size=(1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(1,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [512, 64] X [1, 1].

from user code:
   File "<string>", line 28, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''