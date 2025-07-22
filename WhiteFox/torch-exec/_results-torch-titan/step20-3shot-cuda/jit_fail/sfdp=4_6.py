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

    def __init__(self, n_heads=1, num_query=1, num_key=1, num_value=1, embed_dim=1):
        super().__init__()
        self.n_heads = n_heads
        self.num_key = num_key
        self.num_value = num_value
        self.query = torch.nn.Linear(embed_dim, (self.n_heads * num_query), bias=False)
        self.key = torch.nn.Linear(embed_dim, (self.n_heads * num_key), bias=False)
        self.value = torch.nn.Linear(embed_dim, (self.n_heads * num_value), bias=False)

    def forward(self, q, key, value, output_attentions=False):
        q = self.query(q).view(q.size(0), q.size(1), self.n_heads, self.num_query, (- 1))
        k = self.key(key).view(key.size(0), key.size(1), self.n_heads, self.num_key, (- 1))
        v = self.value(value).view(key.size(0), key.size(1), self.n_heads, self.num_value, (- 1))
        q = q.permute(0, 2, 1, 3, 4).contiguous()
        k = k.permute(0, 2, 1, 3, 4).contiguous()
        v = v.permute(0, 2, 1, 3, 4).contiguous()
        y = (q @ k.transpose((- 2), (- 1)))
        y = (y * ((self.num_key // self.n_heads) ** (- 0.5)))
        if output_attentions:
            attn_weight = torch.softmax(y, dim=(- 1))
            y = (attn_weight @ v)
            attn_weight = attn_weight.view(q.size(0), (- 1), q.size(3)).sum(dim=1)
            return (y.view(q.size(0), (- 1), (self.n_heads * self.num_value)), attn_weight)
        else:
            y = (torch.softmax(y, dim=(- 1)) @ v)
            y = y.view(q.size(0), q.size(2), (self.n_heads * self.num_value))
        return y



func = Model(n_heads=8).to('cuda')



q = torch.randn(16, 8, 48)



key = torch.randn(16, 25, 48)



value = torch.randn(16, 25, 48)


test_inputs = [q, key, value]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (128x48 and 1x8)

jit:
Failed running call_module L__self___query(*(FakeTensor(..., device='cuda:0', size=(16, 8, 48)),), **{}):
a and b must have same reduction dim, but got [128, 48] X [1, 8].

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''