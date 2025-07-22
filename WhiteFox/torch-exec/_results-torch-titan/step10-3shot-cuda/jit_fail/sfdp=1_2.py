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

    def __init__(self, num_heads, d_model, dropout_p=0.1):
        super().__init__()
        self.num_heads = num_heads
        self.d_model = d_model
        self.dropout_p = dropout_p
        self.q_linear = torch.nn.Linear(d_model, d_model)
        self.k_linear = torch.nn.Linear(d_model, d_model)
        self.v_linear = torch.nn.Linear(d_model, d_model)
        self.dropout = torch.nn.Dropout(dropout_p)
        self.out = torch.nn.Linear(d_model, d_model)

    def forward(self, x1, x2, x3):
        q = self.q_linear(x1)
        k = self.k_linear(x2)
        v = self.v_linear(x3)
        q = q.view(q.size(0), q.size(1), self.num_heads, (q.size(2) // self.num_heads)).permute(0, 2, 1, 3)
        k = k.view(k.size(0), k.size(1), self.num_heads, (k.size(2) // self.num_heads)).permute(0, 2, 1, 3)
        v = v.view(v.size(0), v.size(1), self.num_heads, (v.size(2) // self.num_heads)).permute(0, 2, 1, 3)
        q = q.reshape(q.size(0), q.size(1), (- 1))
        k = k.reshape(k.size(0), k.size(1), (- 1))
        v = v.reshape(v.size(0), v.size(1), (- 1))
        scaled_qk = torch.matmul(q, k.transpose((- 2), (- 1)))
        scaled_qk = scaled_qk.div(math.sqrt((self.d_model // self.num_heads)))
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = self.dropout(softmax_qk)
        result = torch.matmul(dropout_qk, v)
        result = result.reshape(result.size(0), result.size(1), self.num_heads, (- 1)).permute(0, 2, 1, 3)
        result = result.reshape(result.size(0), (- 1), result.size(3))
        out = self.out(result)
        return out



num_heads = 1
d_model = 1

func = Model(num_heads, d_model).to('cuda')



x1 = torch.randn(2, 4, 8)



x2 = torch.randn(2, 4, 8)



x3 = torch.randn(2, 4, 8)


test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (8x8 and 1x1)

jit:
Failed running call_module L__self___q_linear(*(FakeTensor(..., device='cuda:0', size=(2, 4, 8)),), **{}):
a and b must have same reduction dim, but got [8, 8] X [1, 1].

from user code:
   File "<string>", line 29, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''