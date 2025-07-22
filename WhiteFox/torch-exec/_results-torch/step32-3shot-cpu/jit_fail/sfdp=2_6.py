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
        self.num_heads = 4
        self.head_dimension = 64
        self.query = torch.nn.Linear(self.head_dimension, self.head_dimension)
        self.key = torch.nn.Linear(self.head_dimension, self.head_dimension)
        self.value = torch.nn.Linear(self.head_dimension, self.head_dimension)
        self.softmax = torch.nn.Softmax(dim=-1)
        self.dropout = torch.nn.Dropout(0.1)

    def forward(self, q, k, v, scale_factor):
        q = self.query(q).reshape((q.shape[0], self.num_heads, -1))
        k = self.key(k).reshape((k.shape[0], self.num_heads, -1))
        v = self.value(v).reshape((v.shape[0], self.num_heads, -1))
        q = q.transpose(-2, -1)
        k = k.transpose(-2, -1)
        v = v.transpose(-2, -1)
        qk = torch.matmul(q, k)
        scaled_qk = qk.div(scale_factor)
        softmax_qk = self.softmax(scaled_qk)
        dropout_qk = self.dropout(softmax_qk)
        output = dropout_qk.matmul(value)
        return output.reshape((q.shape[0], -1))


func = Model().to('cpu')


x1 = torch.randn(1, 24, 128)

x2 = torch.randn(1, 8, 128)

x3 = torch.randn(1, 8, 128)
q = 1

test_inputs = [x1, x2, x3, q]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (24x128 and 64x64)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 24, 128)), Parameter(FakeTensor(..., size=(64, 64), requires_grad=True)), Parameter(FakeTensor(..., size=(64,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [24, 128] X [64, 64].

from user code:
   File "<string>", line 26, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''