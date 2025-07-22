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

    def __init__(self, embedding_dim, num_heads):
        super().__init__()
        self.embedding_dim = embedding_dim
        self.num_heads = num_heads
        hidden_dim = embedding_dim * num_heads
        self.query_proj = torch.nn.Linear(embedding_dim, hidden_dim)
        self.key_proj = torch.nn.Linear(embedding_dim, hidden_dim)
        self.value_proj = torch.nn.Linear(embedding_dim, hidden_dim)
        self.output_proj = torch.nn.Linear(hidden_dim, embedding_dim)

    def forward(self, query, key, value, padding_mask):
        (B, T, C) = query.shape
        H = self.num_heads
        query = self.query_proj(query).view(B, T, H, C)
        key = self.key_proj(key).view(B, T, H, C)
        value = self.value_proj(value).view(B, T, H, C)
        padding_mask = padding_mask.view(B, 1, T, 1)
        query = query.view(B, T, H, C, 1)
        key = key.view(B, T, H, 1, C)
        value = value.view(B, T, H, 1, C)
        padding_mask = padding_mask.view(B, 1, 1, T, T)
        qk = query * key
        inv_scale_factor = math.sqrt(C)
        scaled_qk = qk / inv_scale_factor
        softmax_qk = scaled_qk.softmax(dim=2)
        dropout_p = 0
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk * value
        output = output.transpose(1, 2)
        output_shape = (B, H, T, C)
        output = output.reshape(*output_shape)
        output = self.output_proj(output)
        return output


embedding_dim = 1
num_heads = 1
func = Model(128, 8).to('cpu')


x1 = torch.randn(3, 4, 128)

x2 = torch.randn(3, 4, 128)

x3 = torch.randn(3, 4, 128)

x4 = torch.randint(2, (3, 1, 4))

test_inputs = [x1, x2, x3, x4]

# JIT_FAIL
'''
direct:
shape '[3, 1, 1, 4, 4]' is invalid for input of size 12

jit:
Failed running call_method view(*(FakeTensor(..., size=(3, 1, 4, 1), dtype=torch.int64), 3, 1, 1, 4, 4), **{}):
shape '[3, 1, 1, 4, 4]' is invalid for input of size 12

from user code:
   File "<string>", line 35, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''