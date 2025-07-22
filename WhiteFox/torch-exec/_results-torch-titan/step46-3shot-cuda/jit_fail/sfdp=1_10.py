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

    def __init__(self, num_heads):
        super().__init__()
        self.num_heads = num_heads
        self.query_projection = torch.nn.Linear(3, self.num_heads)
        self.key_projection = torch.nn.Linear(3, self.num_heads)
        self.value_projection = torch.nn.Linear(3, self.num_heads)

    def forward(self, query, key, value, dropout_p):
        q = self.query_projection(query)
        k = self.key_projection(key)
        v = self.value_projection(value)
        qk = torch.matmul(q, k.transpose((- 2), (- 1)))
        inv_scale_factor = torch.float32((1.0 / np.sqrt(float(q.shape[(- 1)]))))
        scaled_qk = qk.div(inv_scale_factor)
        dropout_qk = torch.nn.functional.dropout(scaled_qk, p=dropout_p)
        return dropout_qk.matmul(v)



num_heads = 1

func = Model(num_heads).to('cuda')



query = torch.randn(4, 3, 60)



key = torch.randn(4, 120, 3)



value = torch.randn(4, 120, 3)

dropout_p = 1

test_inputs = [query, key, value, dropout_p]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (12x60 and 3x1)

jit:
Failed running call_module L__self___query_projection(*(FakeTensor(..., device='cuda:0', size=(4, 3, 60)),), **{}):
a and b must have same reduction dim, but got [12, 60] X [3, 1].

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''