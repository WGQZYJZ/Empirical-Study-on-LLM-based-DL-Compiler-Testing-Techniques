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



class MultiHeadedAttention(nn.Module):

    def __init__(self, embed_dim, num_heads):
        super().__init__()
        self.head_dim = (embed_dim // num_heads)
        self.num_heads = num_heads
        self.linear_k = nn.Linear(embed_dim, embed_dim)
        self.linear_v = nn.Linear(embed_dim, embed_dim)
        self.linear_q = nn.Linear(embed_dim, embed_dim)
        self.linear_final = nn.Linear(embed_dim, embed_dim)

    def forward(self, query, key, value, attn_mask):
        key = self.linear_k(key)
        value = self.linear_v(value)
        query = self.linear_q(query)
        dim = query.dim()
        transpose_a = (dim == 2)
        transpose_b = (dim == 1)
        key = key.transpose((- 2), (- 1))
        attn_weight = (torch.bmm(query, key) / math.sqrt(query.size((- 1))))
        if (attn_mask is not None):
            attn_mask = attn_mask.unsqueeze(0).unsqueeze(0)
            attn_mask = attn_mask.expand(attn_weight.shape[0], (- 1), (- 1))
            attn_weight += attn_mask
        attn_weight = F.softmax(attn_weight, dim=(- 1))
        attn = torch.bmm(attn_weight, value)
        if transpose_a:
            attn = attn.transpose(1, 0)
        if transpose_b:
            attn = attn.transpose(1, 0)
        return self.linear_final(attn)



embed_dim = 1
num_heads = 1
func = MultiHeadedAttention(10, 3).to('cuda')



query = torch.randn(1, 4, 10)



key = torch.randn(1, 6, 10)



value = torch.randn(1, 6, 10)



attn_mask = torch.ones(1, 1, 1)


test_inputs = [query, key, value, attn_mask]

# JIT_FAIL
'''
direct:
expand(torch.cuda.FloatTensor{[1, 1, 1, 1, 1]}, size=[1, -1, -1]): the number of sizes provided (3) must be greater or equal to the number of dimensions in the tensor (5)

jit:
Failed running call_method expand(*(FakeTensor(..., device='cuda:0', size=(1, 1, 1, 1, 1)), 1, -1, -1), **{}):
expand: the requested shape has too few dimensions!

from user code:
   File "<string>", line 37, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''