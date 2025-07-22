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

    def __init__(self, num_heads, query_len, hidden_size, dropout):
        super().__init__()
        self.num_heads = num_heads
        self.query = torch.nn.Parameter(torch.zeros(num_heads, query_len, hidden_size))
        self.key = torch.nn.Parameter(torch.zeros(num_heads, query_len, hidden_size))
        self.value = torch.nn.Parameter(torch.zeros(num_heads, query_len, hidden_size))
        self.dropout = dropout

    def forward(self, query, key, value, batch_size):
        x1 = torch.matmul(query, key.transpose((- 2), (- 1)))
        inv_scale_factor = torch.rsqrt(torch.tensor(float(self.head_size), dtype=torch.float32))
        v1 = x1.div(inv_scale_factor)
        v2 = torch.nn.functional.softmax(v1, dim=(- 1))
        v3 = torch.nn.functional.dropout(v2, p=self.dropout)
        return torch.matmul(v3, value).reshape(batch_size, (- 1), v3.shape[(- 1)])



num_heads = 1
query_len = 1
hidden_size = 1
dropout = 1
func = Model(4, 16, 128, 0.5).to('cuda')



query = torch.randn(64, 16, 128)



key = torch.randn(64, 16, 128)



value = torch.randn(64, 16, 128)

batch_size = 1

test_inputs = [query, key, value, batch_size]

# JIT_FAIL
'''
direct:
'Model' object has no attribute 'head_size'

jit:
head_size

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''