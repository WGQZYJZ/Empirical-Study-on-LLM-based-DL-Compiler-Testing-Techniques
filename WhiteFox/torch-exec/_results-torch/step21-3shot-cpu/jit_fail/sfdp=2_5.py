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

    def __init__(self, dropout_p, d_k, d_model, n_heads, scale_factor):
        super().__init__()
        self.dropout1 = torch.nn.Dropout(dropout_p)
        self.dropout2 = torch.nn.Dropout(dropout_p)
        self.d_k = d_k
        self.d_model = d_model
        self.n_heads = n_heads
        self.linear1 = torch.nn.Linear(d_model, d_k * n_heads)
        self.linear2 = torch.nn.Linear(d_model, d_k * n_heads)
        self.linear3 = torch.nn.Linear(d_k * n_heads, d_model)
        self.scale_factor = scale_factor

    def forward(self, q, k, v):
        x1 = self.linear1(q).view(q.size(0), q.size(1), self.n_heads, self.d_k)
        x2 = self.linear2(k).view(k.size(0), k.size(1), self.n_heads, self.d_k)
        x3 = self.linear3(v).view(v.size(0), v.size(1), self.n_heads, self.d_k)
        qk = torch.matmul(x1, x2.transpose(-2, -1))
        scaled_qk = qk.div(self.scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = self.dropout1(softmax_qk)
        output = self.dropout2(torch.matmul(dropout_qk, x3).view(v.size(0), v.size(1), self.n_heads * self.d_k))
        return output


dropout_p = 1
d_k = 1
d_model = 1
n_heads = 1
scale_factor = 1

func = Model(dropout_p, d_k, d_model, n_heads, scale_factor).to('cpu')


x1 = torch.randn(1, 2, 3, 256)

x2 = torch.randn(1, 2, 2, 256)

x3 = torch.randn(1, 2, 3, 256)

test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (6x256 and 1x1)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 2, 3, 256)), Parameter(FakeTensor(..., size=(1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(1,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [6, 256] X [1, 1].

from user code:
   File "<string>", line 28, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''