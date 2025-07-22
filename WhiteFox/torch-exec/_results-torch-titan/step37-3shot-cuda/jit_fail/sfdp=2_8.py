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

    def __init__(self, d_input, d_model, dropout_p):
        super().__init__()
        self.dropout_p = dropout_p
        self.q_linear = torch.nn.Linear(d_input, d_model)
        self.k_linear = torch.nn.Linear(d_input, d_model)
        self.v_linear = torch.nn.Linear(d_input, d_model)
        self.dropout = torch.nn.Dropout(dropout_p)

    def forward(self, query, key, value, inv_scale_factor):
        q = self.q_linear(query)
        k = self.k_linear(key)
        v = self.v_linear(value)
        qk = torch.matmul(q, k.transpose((- 2), (- 1)))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = self.dropout(softmax_qk)
        return dropout_qk.matmul(v)



d_input = 1
d_model = 1
dropout_p = 1

func = Model(d_input, d_model, dropout_p).to('cuda')



query = torch.randn(1, 3)



key = torch.randn(2, 6)



value = torch.randn(2, 6)



inv_scale_factor = torch.tensor(4.0)


test_inputs = [query, key, value, inv_scale_factor]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x3 and 1x1)

jit:
Failed running call_module L__self___q_linear(*(FakeTensor(..., device='cuda:0', size=(1, 3)),), **{}):
a and b must have same reduction dim, but got [1, 3] X [1, 1].

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''