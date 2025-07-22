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

    def __init__(self, *, depth, num_heads):
        super().__init__()
        if ((depth % num_heads) != 0):
            raise ValueError('The dimensionality of the input tensor must be divisible by num_heads.')
        self.depth = depth
        self.num_heads = num_heads
        self.qkv = torch.nn.Linear(self.depth, (self.depth * 3))

    def split_heads(self, x):
        depth_per_head = (self.depth // self.num_heads)
        shape = (x.shape[:(- 1)] + (self.num_heads, depth_per_head))
        x = torch.reshape(x, shape)
        return x.transpose((- 3), (- 2))

    def forward(self, x, mask):
        qkv = self.qkv(x)
        (query, key, value) = torch.split(x, self.depth, (- 1))
        num_batch = query.shape[0]
        query = self.split_heads(query)
        key = self.split_heads(key)
        value = self.split_heads(value)
        mask = mask.expand(num_batch, num_heads, query.shape[2], query.shape[2])
        v1 = torch.matmul(query, key.transpose((- 2), (- 1)))
        inv_scale_factor = ((self.depth // self.num_heads).item() ** (- 0.5))
        v2 = v1.div(inv_scale_factor)
        v3 = F.softmax(v2, dim=(- 1))
        v4 = F.dropout(v3, p=dropout_p)
        v5 = torch.matmul(v4, value)
        v6 = torch.flatten(v5, start_dim=1)
        return v6



func = Model(depth=256, num_heads=1).to('cuda')



x = torch.randn(1, 256)



mask = torch.ones([1, 1, 1, 1])


test_inputs = [x, mask]

# JIT_FAIL
'''
direct:
not enough values to unpack (expected 3, got 1)

jit:


from user code:
   File "<string>", line 33, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''