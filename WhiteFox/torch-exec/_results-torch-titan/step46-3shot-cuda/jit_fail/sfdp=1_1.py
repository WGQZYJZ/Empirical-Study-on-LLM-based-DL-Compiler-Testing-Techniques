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

    def __init__(self, embed_dim, num_heads, dim_feedforward, dropout_p):
        super().__init__()
        self.qkv = torch.nn.Linear(embed_dim, (3 * embed_dim))
        self.linear1 = torch.nn.Linear((3 * embed_dim), dim_feedforward)
        self.dropout = torch.nn.Dropout(p=dropout_p)
        self.linear2 = torch.nn.Linear(dim_feedforward, embed_dim)

    def forward(self, x1):
        qkv = self.qkv(x1)
        (q, k, v) = qkv.chunk(3, dim=(- 1))
        output = self.dropout(((q * k) / math.sqrt(k.size((- 1)))))
        output = self.dropout(self.linear2(self.dropout(self.linear1(output))))
        return output



embed_dim = 1
num_heads = 1
dim_feedforward = 1
dropout_p = 1

func = Model(embed_dim, num_heads, dim_feedforward, dropout_p).to('cuda')



x1 = torch.randn(1, 1, 4096)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x4096 and 1x3)

jit:
Failed running call_module L__self___qkv(*(FakeTensor(..., device='cuda:0', size=(1, 1, 4096)),), **{}):
a and b must have same reduction dim, but got [1, 4096] X [1, 3].

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''