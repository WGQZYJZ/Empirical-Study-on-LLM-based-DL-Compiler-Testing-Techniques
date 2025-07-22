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

    def __init__(self, d_model, num_heads):
        super().__init__()
        self.d_k = (d_model // num_heads)
        self.num_heads = num_heads
        self.fc_q = torch.nn.Linear(d_model, d_model)
        self.fc_k = torch.nn.Linear(d_model, d_model)
        self.fc_v = torch.nn.Linear(d_model, d_model)
        self.fc_o = torch.nn.Linear(d_model, d_model)

    def attention(self, query, key, value):
        inv_scale = (1.0 / (self.d_k ** 0.5))
        attention = scaled_dot_product_attention(query, key, value, inv_scale)
        return attention

    def forward(self, q, k, v):
        q = self.fc_q(q).view(q.shape[0], (- 1), self.num_heads, self.d_k)
        k = self.fc_k(k).view(q.shape[0], (- 1), self.num_heads, self.d_k)
        v = self.fc_v(v).view(q.shape[0], (- 1), self.num_heads, self.d_k)
        q = q.permute(2, 0, 1, 3)
        k = k.permute(2, 0, 1, 3)
        v = v.permute(2, 0, 1, 3)
        a = self.attention(q, k, v)
        a = a.permute(1, 2, 0, 3).contiguous().view(a.shape[1], (- 1), a.shape[3])
        o = self.fc_o(a)
        return o




class Model(torch.nn.Module):

    def __init__(self, d_model=768, num_heads=8):
        super().__init__()
        self.mha = MultiHeadAttention(d_model, num_heads)

    def forward(self, x1, x2):
        y = self.mha(x1, x2, x2)
        return y



func = Model().to('cuda')



x1 = torch.randn(2, 16, 768)



x2 = torch.randn(2, 16, 768)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
name 'scaled_dot_product_attention' is not defined

jit:
name 'scaled_dot_product_attention' is not defined

from user code:
   File "<string>", line 53, in forward
  File "/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/torch/nn/modules/module.py", line 1527, in _call_impl
    return forward_call(*args, **kwargs)
  File "<string>", line 38, in forward
  File "<string>", line 28, in attention


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''