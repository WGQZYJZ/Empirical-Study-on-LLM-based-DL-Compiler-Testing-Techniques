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

    def __init__(self, d_model, num_heads, dropout_p):
        super().__init__()
        self.query_layer = torch.nn.Linear(d_model, d_model)
        self.key_layer = torch.nn.Linear(d_model, d_model)
        self.value_layer = torch.nn.Linear(d_model, d_model)
        self.dropout = torch.nn.Dropout(dropout_p)

    def forward(self, q, k, v):
        q = self.query_layer(q)
        k = self.key_layer(k)
        v = self.value_layer(v)
        qk = torch.matmul(q, k.transpose(-2, -1))
        scaled_qk = qk.div(math.sqrt(torch.tensor(k.size(-1))))
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = self.dropout(softmax_qk)
        output = dropout_qk.matmul(v)
        return output


d_model = 1
num_heads = 1
dropout_p = 1

func = Model(d_model, num_heads, dropout_p).to('cpu')


q = torch.randn(1, 16, 128)

k = torch.randn(1, 32, 128)

v = torch.randn(1, 32, 128)

test_inputs = [q, k, v]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (16x128 and 1x1)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 16, 128)), Parameter(FakeTensor(..., size=(1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(1,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [16, 128] X [1, 1].

from user code:
   File "<string>", line 23, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''