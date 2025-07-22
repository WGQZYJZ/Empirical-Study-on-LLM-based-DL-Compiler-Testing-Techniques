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

    def __init__(self, num_heads, qkv_dim):
        super().__init__()
        self.num_heads = num_heads
        self.qkv_dim = qkv_dim
        self.scale_factor = ((qkv_dim / num_heads) ** 0.5)
        self.query = torch.nn.Linear(qkv_dim, qkv_dim)
        self.key = torch.nn.Linear(qkv_dim, qkv_dim)
        self.value = torch.nn.Linear(qkv_dim, qkv_dim)
        self.dropout = torch.nn.Dropout(dropout_p)

    def forward(self, x1, x2):
        q = self.query(x1)
        k = self.key(x2).transpose((- 2), (- 1))
        v = self.value(x2)
        qk = torch.matmul(q, k)
        scaled_qk = qk.mul(self.scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = self.dropout(softmax_qk)
        v1 = dropout_qk.matmul(v)
        return v1



num_heads = 1
qkv_dim = 1

func = Model(num_heads, qkv_dim).to('cuda')

x1 = 1
x2 = 1

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
linear(): argument 'input' (position 1) must be Tensor, not int

jit:
Failed running call_module L__self___query(*(1,), **{}):
linear(): argument 'input' (position 1) must be Tensor, not int

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''