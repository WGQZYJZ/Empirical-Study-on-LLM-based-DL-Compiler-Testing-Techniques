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

    def __init__(self, query_dim, key_dim, value_dim, num_head, dropout):
        super().__init__()
        self.qkv_linear = torch.nn.Linear(query_dim, (query_dim * 3))
        self.linear = torch.nn.Linear((query_dim * num_head), value_dim)

    def forward(self, x1):
        v1 = self.qkv_linear(x1)
        q = v1[:, :query_dim]
        k = v1[:, query_dim:(query_dim * 2)]
        v = v1[:, (query_dim * 2):]
        qk = torch.matmul(q, k.transpose((- 2), (- 1)))
        inv_scale_factor = torch.rsqrt(torch.tensor(query_dim).float())
        softmax_qk = torch.nn.functional.dropout((qk * inv_scale_factor), p=dropout)
        softmax_qk = torch.nn.functional.softmax(softmax_qk, dim=(- 1))
        output = torch.matmul(softmax_qk, v)
        final_v = self.linear(output.transpose(1, 2))
        return final_v



query_dim = 1
key_dim = 1
value_dim = 1
num_head = 1
dropout = 1
func = Model(query_dim, key_dim, value_dim, num_head, dropout).to('cuda')

x1 = 1

test_inputs = [x1]

# JIT_FAIL
'''
direct:
linear(): argument 'input' (position 1) must be Tensor, not int

jit:
Failed running call_module L__self___qkv_linear(*(1,), **{}):
linear(): argument 'input' (position 1) must be Tensor, not int

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''