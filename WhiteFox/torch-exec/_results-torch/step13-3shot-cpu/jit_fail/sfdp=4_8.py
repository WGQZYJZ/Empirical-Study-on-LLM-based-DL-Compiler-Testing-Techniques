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

    def __init__(self, n_head, d_model, d_k, d_v, d_ff):
        super().__init__()
        self.n_head = n_head
        self.d_k = d_k
        self.d_v = d_v
        self.d_model = d_model
        self.d_ff = d_ff
        self.w_qs = torch.nn.Linear(d_model, n_head * d_k)
        self.w_ks = torch.nn.Linear(d_model, n_head * d_k)
        self.w_vs = torch.nn.Linear(d_model, n_head * d_v)
        self.fc = torch.nn.Linear(n_head * d_v, d_model)

    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor, attention_mask: torch.Tensor):
        d_k = self.d_k
        d_v = self.d_v
        n_head = self.n_head
        sz_b = query.size(0)
        len_q = query.size(1)
        len_k = key.size(1)
        len_v = value.size(1)
        query = self.w_qs(query).view(sz_b, len_q, n_head, d_k)
        key = self.w_ks(key).view(sz_b, len_k, n_head, d_k)
        value = self.w_vs(value).view(sz_b, len_v, n_head, d_v)
        query = query.permute(2, 0, 1, 3)
        key = key.permute(2, 0, 1, 3)
        value = value.permute(2, 0, 1, 3)
        x = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(d_k)
        x = x + attention_mask
        x = torch.softmax(x, dim=-1)
        x = torch.matmul(x, value)
        x = x.transpose(1, 2).contiguous().view(sz_b, len_q, -1)
        x = self.fc(x)
        return x


n_head = 1
d_model = 1
d_k = 1
d_v = 1
d_ff = 1

func = Model(n_head, d_model, d_k, d_v, d_ff).to('cpu')


q = torch.randn(5, 10, 10)

k = torch.randn(5, 15, 10)

v = torch.randn(5, 15, 20)


attention_mask = torch.randn(5, 1, 15, 15).ge(1).type(torch.FloatTensor)

test_inputs = [q, k, v, attention_mask]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (50x10 and 1x1)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(5, 10, 10)), Parameter(FakeTensor(..., size=(1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(1,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [50, 10] X [1, 1].

from user code:
   File "<string>", line 35, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''