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

    def __init__(self, query_channels, key_channels, output_channels, num_heads):
        super(MultiHeadAttention, self).__init__()
        self.num_heads = num_heads
        self.key_channels = key_channels
        self.output_channels = output_channels
        self.q_lin = nn.Linear(query_channels, num_heads * key_channels)
        self.k_lin = nn.Linear(key_channels, num_heads * key_channels)
        self.v_lin = nn.Linear(key_channels, num_heads * output_channels)
        self.out_lin = nn.Linear(num_heads * output_channels, output_channels)
        self.dropout = nn.Dropout(0.25)

    def forward(self, query, key, value):
        q = self.q_lin(query)
        k = self.k_lin(key)
        v = self.v_lin(value)
        (q, k, v) = (x.view(x.size(0), x.size(1), self.num_heads, self.key_channels) for x in (q, k, v))
        (scaled_q, scaled_k, scaled_v) = (x.transpose(-2, -1) for x in (q, k, v))
        attn_logits = scaled_q.matmul(scaled_k)
        attn = safe_logsoftmax(attn_logits, dim=-1)
        attn = self.dropout(attn)
        out = attn.matmul(scaled_v)
        out = out.transpose(0, 1).contiguous().view(attn.size(1), -1)
        return self.out_lin(out)

    def extra_repr(self):
        return 'MultiHeadAttention(%d, %d, %d)' % (self.key_channels, self.output_channels, self.num_heads)


query_channels = 1
key_channels = 1
output_channels = 1
num_heads = 1

func = MultiHeadAttention(query_channels, key_channels, output_channels, num_heads).to('cpu')


x1 = torch.randn(2, 3, 64, 64)

x2 = torch.randn(2, 1, 8, 8)
query = 1

test_inputs = [x1, x2, query]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (384x64 and 1x1)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(2, 3, 64, 64)), Parameter(FakeTensor(..., size=(1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(1,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [384, 64] X [1, 1].

from user code:
   File "<string>", line 27, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''