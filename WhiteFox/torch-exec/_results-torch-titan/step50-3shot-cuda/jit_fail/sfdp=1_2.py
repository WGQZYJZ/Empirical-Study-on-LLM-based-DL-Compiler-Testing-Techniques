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

    def __init__(self, num_heads=1, embedding_dim=16, dropout_p=0.6):
        super().__init__()
        self.num_heads = num_heads
        self.depth = ((embedding_dim * num_heads) // 8)
        self.wq = torch.nn.Linear(embedding_dim, (embedding_dim * num_heads))
        self.wk = torch.nn.Linear(embedding_dim, (embedding_dim * num_heads))
        self.wv = torch.nn.Linear(embedding_dim, (embedding_dim * num_heads))
        self.dense = torch.nn.Linear((embedding_dim * num_heads), embedding_dim)

    def split_heads(self, x, batch_size):
        x = x.view(batch_size, (- 1), self.num_heads, self.depth)
        return x.permute(0, 2, 1, 3)

    def forward(self, x1):
        batch_size = x1.shape[0]
        q = self.wq(x1)
        k = self.wk(x1)
        v = self.wv(x1)
        q = self.split_heads(q, batch_size)
        k = self.split_heads(k, batch_size)
        v = self.split_heads(v, batch_size)
        scaled_attention = scaled_dot_product_attention(q, k, v, self.depth)
        scaled_attention = scaled_attention.permute(0, 2, 1, 3)
        concat_attention = scaled_attention.reshape(batch_size, (- 1), (self.depth * self.num_heads))
        output = self.dense(concat_attention)
        return output



func = Model().to('cuda')



x1 = torch.randn(32, 128, 768)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (4096x768 and 16x16)

jit:
Failed running call_module L__self___wq(*(FakeTensor(..., device='cuda:0', size=(32, 128, 768)),), **{}):
a and b must have same reduction dim, but got [4096, 768] X [16, 16].

from user code:
   File "<string>", line 32, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''