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

class MultiheadAttention(torch.nn.Module):

    def __init__(self, embed_dim, num_heads):
        super().__init__()
        self.embed_dim = embed_dim
        self.num_heads = num_heads
        self.head_dim = embed_dim // num_heads
        if self.head_dim * num_heads != self.embed_dim:
            raise ValueError('embed_dim must be divisible by num_heads')
        self.scaling = self.head_dim ** (-0.5)
        self.qk = torch.nn.Linear(embed_dim, embed_dim * 2, bias=False)
        self.v = torch.nn.Linear(embed_dim, embed_dim, bias=False)
        self.output = torch.nn.Linear(embed_dim, embed_dim, bias=False)

    def forward(self, query, value):
        (B, C, T) = query.size()
        T = query.shape[-1]
        qk = self.qk(query).reshape(B, -1, T).transpose(-2, -1)
        value = self.v(value).reshape(B, -1, T).transpose(-2, -1)
        scale_factor = torch.rsqrt(torch.sum(torch.mul(qk, qk), dim=-1))
        scale_factor = scale_factor.view(B, T, 1)
        scaled_qk = qk.mul(scale_factor)
        attention = torch.softmax(scaled_qk, dim=-1)
        dropout_att = torch.nn.functional.dropout(attention, p=0.1, training=self.training)
        value = dropout_att.matmul(value)
        output = self.output(value.transpose(-2, -1).reshape(B, C, T))
        return (output, attention)

class Model(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.multihead_attention = MultiheadAttention(embed_dim=8, num_heads=8)

    def forward(self, query_input, value_input):
        (output, attention) = self.multihead_attention(query_input, value_input)
        return (output, attention)


func = Model().to('cpu')


query_input = torch.randn(1, 32, 8)

value_input = torch.randn(1, 16, 8)

test_inputs = [query_input, value_input]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 64] but got: [1, 8].

jit:
Failed running call_method matmul(*(FakeTensor(..., size=(1, 8, 64)), FakeTensor(..., size=(1, 8, 16))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 64] but got: [1, 8].

from user code:
   File "<string>", line 48, in forward
  File "<string>", line 37, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''