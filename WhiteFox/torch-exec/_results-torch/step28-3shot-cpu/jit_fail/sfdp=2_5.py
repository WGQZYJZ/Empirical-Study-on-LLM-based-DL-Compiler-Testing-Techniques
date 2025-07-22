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

    def __init__(self, n_queries, n_keys, n_values, n_heads):
        super().__init__()
        self.q = torch.nn.Linear(n_queries, n_heads * n_queries)
        self.k = torch.nn.Linear(n_keys, n_heads * n_keys)
        self.v = torch.nn.Linear(n_values, n_heads * n_values)

    def forward(self, q_input, k_input, v_input):
        q = self.q(q_input)
        k = self.k(k_input)
        v = self.v(v_input)
        q = q.view(q.shape[0], -1, n_heads, -1)
        k = k.view(k.shape[0], -1, n_heads, -1)
        v = v.view(v.shape[0], -1, n_heads, -1)
        q = q.transpose(-2, -3)
        k = k.transpose(-2, -3)
        v = v.transpose(-2, -3)
        qk = torch.matmul(q, k.transpose(-2, -1))
        inv_scale_factor = math.sqrt(1.0 / math.sqrt(q_input.shape[-1]) + 1e-06)
        qk = qk.div(inv_scale_factor)
        softmax_qk = torch.nn.functional.softmax(qk, dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.2)
        output = torch.matmul(dropout_qk, v)
        return output


n_queries = 10
n_keys = 10
n_values = 20
n_heads = 3
func = Model(n_queries, n_keys, n_values, n_heads).to('cpu')


n_queries = 10
q_input = torch.randn(5, 6, n_queries)

n_keys = 10
k_input = torch.randn(6, 5, n_keys)

n_values = 20
v_input = torch.randn(6, 5, n_values)

test_inputs = [q_input, k_input, v_input]

# JIT_FAIL
'''
direct:
only one dimension can be inferred

jit:
Failed running call_method view(*(FakeTensor(..., size=(5, 6, 30)), 5, -1, 3, -1), **{}):
only one dimension can be inferred

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''