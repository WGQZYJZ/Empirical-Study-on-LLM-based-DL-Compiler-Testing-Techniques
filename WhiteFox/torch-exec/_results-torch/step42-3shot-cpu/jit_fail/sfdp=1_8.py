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

    def __init__(self, d_model, nhead, dropout=0.2):
        super().__init__()
        self.nhead = nhead
        self.d_k = d_model // nhead
        self.dropout = dropout
        self.q_proj = torch.nn.Linear(d_model, d_model)
        self.k_proj = torch.nn.Linear(d_model, d_model)
        self.v_proj = torch.nn.Linear(d_model, d_model)
        self.out_proj = torch.nn.Linear(d_model, d_model)

    def forward(self, query, key, value):
        q = self.q_proj(query)
        k = self.k_proj(key)
        v = self.v_proj(value)
        q = q.view(q.size(0), q.size(1), self.nhead, self.d_k).transpose(1, 2)
        k = k.view(k.size(0), k.size(1), self.nhead, self.d_k).transpose(1, 2)
        v = v.view(v.size(0), v.size(1), self.nhead, self.d_k).transpose(1, 2)
        qk = torch.matmul(q, k.transpose(2, 3))
        qk = qk.div(math.sqrt(self.d_k))
        qk = qk.softmax(dim=-1)
        qk = torch.nn.functional.dropout(qk, p=self.dropout)
        output = torch.matmul(qk, v)
        output = output.transpose(1, 2).contiguous().view(output.size(0), output.size(1), output.size(2) * output.size(3))
        return output


d_model = 1
nhead = 1

func = Model(d_model, nhead).to('cpu')


x1 = torch.randn(5, 60, 512)

x2 = torch.randn(5, 150, 512)

x3 = torch.randn(5, 150, 512)

test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (300x512 and 1x1)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(5, 60, 512)), Parameter(FakeTensor(..., size=(1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(1,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [300, 512] X [1, 1].

from user code:
   File "<string>", line 26, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''