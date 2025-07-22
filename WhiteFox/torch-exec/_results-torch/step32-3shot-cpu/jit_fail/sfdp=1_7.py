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

class Scaled_Dot_Attention(torch.nn.Module):

    def __init__(self, d_model, q_dim, k_dim, dropout_p):
        super().__init__()
        self.q = torch.nn.Linear(q_dim, k_dim, bias=False)
        self.k = torch.nn.Linear(k_dim, k_dim, bias=False)
        self.v = torch.nn.Linear(d_model, k_dim, bias=False)
        self.dr_k = torch.nn.Dropout(dropout_p)
        self.dr_v = torch.nn.Dropout(dropout_p)
        self.softmax = torch.nn.Softmax(dim=1)
        self.inv_scale_factor = torch.nn.Parameter(torch.tensor(1.0 / k_dim ** 0.5))

    def forward(self, queries, keys, values):
        q = self.q(queries)
        k = self.k(keys)
        v = self.v(values)
        q_k = torch.matmul(q, k.transpose(-2, -1))
        scaled_q_k = q_k.div(self.inv_scale_factor)
        dr_scaled_q_k = self.dr_k(scaled_q_k)
        softmax_scaled_q_k = self.softmax(dr_scaled_q_k)
        dropout_softmax_scaled_q_k = self.dr_v(softmax_scaled_q_k)
        output = torch.matmul(dropout_softmax_scaled_q_k, v)
        return output

class Model(torch.nn.Module):

    def __init__(self, d_model, q_dim, k_dim, dropout_p):
        super().__init__()
        self.scaled_dot_attention = Scaled_Dot_Attention(d_model, q_dim, k_dim, dropout_p)

    def forward(self, x1, x2):
        output = self.scaled_dot_attention(x1, x2, x2)
        return output


d_model = 8
q_dim = 8
k_dim = 8
dropout_p = 0.01
func = Model(d_model, q_dim, k_dim, dropout_p).to('cpu')


x1 = torch.randn(1, 3, 10)

x2 = torch.randn(1, 3, 18)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (3x10 and 8x8)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 3, 10)), Parameter(FakeTensor(..., size=(8, 8), requires_grad=True)), None), **{}):
a and b must have same reduction dim, but got [3, 10] X [8, 8].

from user code:
   File "<string>", line 44, in forward
  File "<string>", line 26, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''