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

class MultiHeadAttention(nn.Module):

    def __init__(self, d_model, heads):
        super().__init__()
        self.d_model = d_model
        self.heads = heads
        self.scale = torch.sqrt(torch.FloatTensor([d_model])).item()
        self.query_projection = nn.Linear(d_model, d_model)
        self.key_projection = nn.Linear(d_model, d_model)
        self.value_projection = nn.Linear(d_model, d_model)

    def forward(self, query, key, value, mask=None):
        scale = self.scale
        batch_size = query.shape[0]
        N = value.shape[0]
        query = self.query_projection(query).view(batch_size, N, self.heads, self.d_model // self.heads).transpose(-2, -3)
        key = self.key_projection(key).view(batch_size, N, self.heads, self.d_model // self.heads).transpose(-2, -3)
        value = self.value_projection(value).view(batch_size, N, self.heads, self.d_model // self.heads).transpose(-2, -3)
        attn_weights = torch.matmul(query, key.transpose(-2, -1)) / scale
        if mask is not None:
            attn_weights.masked_fill(mask == 0, -1000000000.0)
        attn_weights = attn_weights.softmax(dim=-1)
        context = torch.matmul(attn_weights, value)
        context = context.transpose(-2, -3)
        new_shape = [*context.shape[:-2], self.d_model]
        context = context.reshape(new_shape)
        return context


d_model = 1
heads = 1

func = MultiHeadAttention(d_model, heads).to('cpu')


query_tensor = torch.randn(4, 49, 512)

key_tensor = torch.randn(4, 49, 512)

value_tensor = torch.randn(4, 49, 512)

mask = torch.ones(4, 49, 49)

test_inputs = [query_tensor, key_tensor, value_tensor, mask]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (196x512 and 1x1)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(4, 49, 512)), Parameter(FakeTensor(..., size=(1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(1,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [196, 512] X [1, 1].

from user code:
   File "<string>", line 28, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''