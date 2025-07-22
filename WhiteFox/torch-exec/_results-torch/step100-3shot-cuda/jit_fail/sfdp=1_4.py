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

class Attention(torch.nn.Module):

    def __init__(self, dim, num_heads=2, dropout_p=0.66):
        super().__init__()
        self.num_heads = num_heads
        self.dim = dim
        self.query = torch.nn.Linear(dim, dim, bias=True)
        self.key = torch.nn.Linear(dim, dim, bias=True)
        self.value = torch.nn.Linear(dim, dim, bias=True)

    def forward(self, query, key, value, *args, mask=None, **kwargs):
        n = self.num_heads
        c = self.dim
        h = query.shape[1]
        q = self.query(query).view(n, c, h).transpose(-2, -1).unsqueeze(1)
        k = self.key(key).view(n, c, h).transpose(-2, -1).unsqueeze(1)
        v = self.value(value).view(n, c, h).transpose(-2, -1).unsqueeze(1)
        attn = torch.matmul(q, k.transpose(-2, -1)) / c ** 0.5
        if mask is not None and mask.numel() > 0:
            mask = mask.repeat(n, 1, 1)
            attn = attn.masked_fill(mask == 0, -1e+38)
        attn = attn.softmax(dim=-1)
        attn = torch.nn.functional.dropout(attn, p=0.66, training=self.training)
        ctxt = attn.matmul(v).squeeze(1)
        batch_size = query.size(0)
        num_query = query.size(1)
        dim = self.dim
        output = ctxt.contiguous().view(batch_size, num_query, h * c)
        return (output, attn)


dim = 1

func = Attention(dim).to('cuda')


x1 = torch.randn(1, 32, 64)

x2 = torch.randn(1, 32, 64)

x3 = torch.randn(1, 32, 64)

test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (32x64 and 1x1)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., device='cuda:0', size=(1, 32, 64)), Parameter(FakeTensor(..., device='cuda:0', size=(1, 1), requires_grad=True)), Parameter(FakeTensor(..., device='cuda:0', size=(1,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [32, 64] X [1, 1].

from user code:
   File "<string>", line 27, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''