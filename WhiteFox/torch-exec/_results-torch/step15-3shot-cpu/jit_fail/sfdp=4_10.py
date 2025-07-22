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

    def __init__(self, num_queries, num_keys, num_values, num_heads):
        super().__init__()
        self.num_heads = num_heads
        self.num_queries = num_queries
        self.num_keys = num_keys
        self.num_values = num_values
        self.query_projection = torch.nn.Linear(num_queries, num_queries)
        self.key_projection = torch.nn.Linear(num_keys, num_keys)
        self.value_projection = torch.nn.Linear(num_values, num_values)

    def scaled_dot_product_attention(self, query, key, value, attn_mask):
        s = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        s += attn_mask
        attn_weights = torch.softmax(s, dim=-1)
        return attn_weight @ value

    def forward(self, query, key, value, attn_mask):
        query = self.query_projection(query)
        key = self.key_projection(key)
        value = self.value_projection(value)
        return self.scaled_dot_product_attention(query, key, value, attn_mask)


num_queries = 1
num_keys = 1
num_values = 1
num_heads = 1
func = Model(10, 20, 30, 2).to('cpu')


query = torch.randn(4, 10)

key = torch.randn(4, 20)

value = torch.randn(4, 30)

attn_mask = torch.randn(4, 1, 1, 20)

test_inputs = [query, key, value, attn_mask]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (4x10 and 20x4)

jit:
Failed running call_function <built-in function matmul>(*(FakeTensor(..., size=(4, 10)), FakeTensor(..., size=(20, 4))), **{}):
a and b must have same reduction dim, but got [4, 10] X [20, 4].

from user code:
   File "<string>", line 35, in forward
  File "<string>", line 26, in scaled_dot_product_attention


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''