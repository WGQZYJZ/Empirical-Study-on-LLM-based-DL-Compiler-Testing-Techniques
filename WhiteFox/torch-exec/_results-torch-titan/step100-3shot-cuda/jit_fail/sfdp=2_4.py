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

    def __init__(self, dim=512, num_heads=8, dropout=0.0, bias=False):
        super().__init__()
        self.dim = dim
        self.qkv = torch.nn.Linear(dim, (dim * 3), bias=bias)
        self.dropout = torch.nn.Dropout(p=dropout)
        self.normalize_fact = (dim ** (- 0.5))
        self.proj = torch.nn.Linear(dim, dim)

    def forward(self, x1):
        qkv = self.qkv(x1).reshape(x1.size(0), 3, self.dim).transpose((- 2), (- 1))
        q = qkv[..., :self.dim]
        k = qkv[..., self.dim:(self.dim * 2)]
        v = qkv[..., (self.dim * 2):]
        (q, k, v) = [x.transpose((- 2), (- 1)) for x in (q, k, v)]
        scaled_qk = (torch.matmul(q, k) * self.normalize_fact)
        dropout_qk = self.dropout(torch.nn.functional.softmax(scaled_qk, dim=(- 1)))
        output = torch.matmul(dropout_qk, v).transpose((- 2), (- 1))
        return self.proj(output)



func = Model().to('cuda')



x1 = torch.randn(1, 128, 512)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
shape '[1, 3, 512]' is invalid for input of size 196608

jit:
Failed running call_method reshape(*(FakeTensor(..., device='cuda:0', size=(1, 128, 1536)), 1, 3, 512), **{}):
shape '[1, 3, 512]' is invalid for input of size 196608

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''