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

class MultiHeadAttention(torch.nn.Module):

    def __init__(self, num_heads, embed_dim, dropout=0.1):
        super().__init__()
        self.num_heads = num_heads
        self.head_dim = embed_dim // num_heads
        self.all_head_dim = self.head_dim * num_heads
        self.embed_dim = embed_dim
        self.dropout_p = dropout
        self.query = torch.nn.Linear(embed_dim, self.all_head_dim)
        self.key = torch.nn.Linear(embed_dim, self.all_head_dim)
        self.value = torch.nn.Linear(embed_dim, self.all_head_dim)
        self.out = torch.nn.Linear(embed_dim, self.all_head_dim)

    def forward(self, query, key, value, key_padding_mask=None, need_weights=True):
        mixed_query = self.query(query)
        mixed_key = self.key(key)
        mixed_value = self.value(value)
        query_shape = query.shape[:-1]
        key_shape = key.shape[:-1]
        mixed_shape = mixed_query.shape[:-1]
        query_group = mixed_query.view(*mixed_shape, self.num_heads, self.head_dim)
        key_group = mixed_key.view(*mixed_shape, self.num_heads, self.head_dim)
        value_group = mixed_value.view(*mixed_shape, self.num_heads, self.head_dim)
        qk = torch.matmul(query_group, key_group.transpose(-2, -1))
        qk_scale = qk.div(self.head_dim ** 0.5)
        if key_padding_mask is not None:
            qk_scale.masked_fill_(key_padding_mask, float('-inf'))
        softmax_qk = torch.nn.functional.softmax(qk_scale, dim=-1)
        softmax_qk_dropout = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = softmax_qk_dropout.matmul(value_group)
        output = output.contiguous().view(*mixed_shape, self.all_head_dim)
        return self.out(output)


num_heads = 1
embed_dim = 1
func = MultiHeadAttention(8, 32).to('cpu')


query = torch.randn(1, 8, 32)

key = torch.randn(1, 16, 32)

value = torch.randn(1, 16, 32)

key_padding_mask = torch.tensor([[0, 0, 0, 1, 1, 0, 0]])

test_inputs = [query, key, value, key_padding_mask]

# JIT_FAIL
'''
direct:
shape '[1, 8, 8, 4]' is invalid for input of size 512

jit:
Failed running call_method view(*(FakeTensor(..., size=(1, 16, 32)), 1, 8, 8, 4), **{}):
shape '[1, 8, 8, 4]' is invalid for input of size 512

from user code:
   File "<string>", line 35, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''