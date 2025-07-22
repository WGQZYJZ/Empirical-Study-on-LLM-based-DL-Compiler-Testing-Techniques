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

    def __init__(self, embedding_dim, num_heads, dropout_p):
        super().__init__()
        self.embedding_dim = embedding_dim
        self.num_heads = num_heads
        self.dropout_p = dropout_p
        self.W_q = torch.nn.Linear(embedding_dim, num_heads * embedding_dim, bias=False)
        self.W_k = torch.nn.Linear(embedding_dim, num_heads * embedding_dim, bias=False)
        self.W_v = torch.nn.Linear(embedding_dim, num_heads * embedding_dim, bias=False)
        self.dropout = torch.nn.Dropout(dropout_p)

    def forward(self, query, key, value, key_padding_mask, training):
        batch_size = query.shape[0]
        q = self.W_q(query)
        k = self.W_k(key)
        v = self.W_v(value)
        q = q.reshape(batch_size, q.shape[1], self.num_heads, -1)
        k = k.reshape(batch_size, k.shape[1], self.num_heads, -1)
        v = v.reshape(batch_size, v.shape[1], self.num_heads, -1)
        scaled_dot_product = torch.einsum('bhie,bhje->bhij', q, k)
        inv_scale_factor = 1 / math.sqrt(torch.tensor(self.embedding_dim, dtype=torch.float32))
        scaled_dot_product = scaled_dot_product.div(inv_scale_factor)
        softmax_scaled_dot_product = scaled_dot_product.softmax(dim=-1)
        dropout_softmax_scaled_dot_product = self.dropout(softmax_scaled_dot_product)
        output = torch.matmul(dropout_softmax_scaled_dot_product, v)
        return output.reshape(batch_size, output.shape[1], -1)


embedding_dim = 64
num_heads = 2
dropout_p = 0.1
func = Model(embedding_dim, num_heads, dropout_p).to('cpu')


query = torch.randn(8, 3, 64)

key = torch.randn(8, 10, 64)

value = torch.randn(8, 10, 64)

key_padding_mask = torch.tensor([[[0, 0, 0, 0, 0, 1, 1, 1, 1, 1]]])
training = 1

test_inputs = [query, key, value, key_padding_mask, training]

# JIT_FAIL
'''
direct:
einsum(): subscript h has size 10 for operand 1 which does not broadcast with previously seen size 3

jit:
Failed running call_function <function einsum at 0x78beed5be040>(*('bhie,bhje->bhij', FakeTensor(..., size=(8, 3, 2, 64)), FakeTensor(..., size=(8, 10, 2, 64))), **{}):
einsum(): subscript h has size 10 for operand 1 which does not broadcast with previously seen size 3

from user code:
   File "<string>", line 33, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''