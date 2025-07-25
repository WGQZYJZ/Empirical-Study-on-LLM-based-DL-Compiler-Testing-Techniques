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

    def __init__(self, d_k: int, d_v: int, num_heads: int, dropout_p: float=0.0):
        super().__init__()
        self.d_k = d_k
        self.d_v = d_v
        self.num_heads = num_heads
        self.dropout_p = dropout_p
        self.head_weight = torch.nn.Linear(d_k, (d_k * num_heads))
        self.key_weight = torch.nn.Linear(d_k, (d_k * num_heads))
        self.value_weight = torch.nn.Linear(d_v, (d_v * num_heads))
        self.output_weight = torch.nn.Linear((num_heads * d_v), d_v)

    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor):
        (q, k, v) = [self.head_weight(q) for q in (query, key, value)]
        (batch_size, seq_length, feature_length) = q.size()
        (other_batch_size, other_seq_length, other_feature_length) = k.size()
        k = self.key_weight(k).view(other_batch_size, other_seq_length, self.num_heads, self.d_k).transpose(0, 1).transpose(1, 2)
        v = self.value_weight(v).view(other_batch_size, other_seq_length, self.num_heads, self.d_v).transpose(0, 1).transpose(1, 2)
        q = q.view(batch_size, seq_length, self.num_heads, self.d_k).transpose(0, 1).transpose(1, 2)
        qk = torch.matmul(q, k).div(math.sqrt(self.d_k))
        inv_scale_factor = (1.0 / sqrt(q.size((- 1))))
        scaled_qk = qk.mul(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = dropout_qk.matmul(v)
        (batch_size, seq_length, num_heads, d_v) = output.size()
        (_, _, _, other_feature_length) = k.size()
        output = output.transpose(0, 1).transpose(1, 2).contiguous().view(seq_length, batch_size, (self.d_v * self.num_heads))
        return self.output_weight(output)



d_k = 1
d_v = 1
num_heads = 1
func = MultiheadAttention(3, 3, 4).to('cuda')



x1 = torch.randn(1, 5, 3)



x2 = torch.randn(1, 5, 3)



x3 = torch.randn(1, 5, 3)


test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (5x12 and 3x12)

jit:
Failed running call_module L__self___key_weight(*(FakeTensor(..., device='cuda:0', size=(1, 5, 12)),), **{}):
a and b must have same reduction dim, but got [5, 12] X [3, 12].

from user code:
   File "<string>", line 32, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''