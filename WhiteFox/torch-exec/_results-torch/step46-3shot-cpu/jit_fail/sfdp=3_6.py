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

    def __init__(self, emb_dim, dropout_p=0.5):
        super().__init__()
        self.dropout_p = dropout_p
        self.query = torch.nn.Linear(emb_dim, emb_dim, bias=False)
        self.key = torch.nn.Linear(emb_dim, emb_dim, bias=False)
        self.value = torch.nn.Linear(emb_dim, emb_dim, bias=False)

    def forward(self, query, key, value):
        q = self.query(query)
        kt = self.key(key).permute(1, 0)
        kv = self.value(value)
        qkt = torch.matmul(q, kt)
        scale = qkt.size(-1) ** (-0.5)
        qkt_scaled = qkt * scale
        dropout_qkt = torch.nn.functional.dropout(qkt_scaled, p=self.dropout_p)
        result = torch.matmul(dropout_qkt, kv)
        return result


emb_dim = 1

func = Model(emb_dim).to('cpu')


query = torch.randn(1, 19, 512)

key = torch.randn(1, 10, 512)

value = torch.randn(1, 10, 512)

test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (19x512 and 1x1)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 19, 512)), Parameter(FakeTensor(..., size=(1, 1), requires_grad=True)), None), **{}):
a and b must have same reduction dim, but got [19, 512] X [1, 1].

from user code:
   File "<string>", line 23, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''