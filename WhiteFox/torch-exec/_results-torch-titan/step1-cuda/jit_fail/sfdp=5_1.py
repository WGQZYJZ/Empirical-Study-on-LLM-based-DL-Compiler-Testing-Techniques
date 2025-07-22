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

    def __init__(self, emb_dim, num_heads):
        super().__init__()
        self.qkv = torch.nn.Linear(emb_dim, (3 * emb_dim))
        self.attn_mask = torch.zeros(20, 20)
        self.dropout = torch.nn.Dropout(0.2)

    def forward(self, x):
        k1 = self.qkv(x)
        q1 = k1[:, :emb_dim]
        k2 = k1[:, (1 * emb_dim)]
        v1 = k1[:, (2 * emb_dim):]
        query = torch.einsum('bih,bij->bhj', q1, k2)
        key = torch.einsum('bij,bic->bjk', q1, v1)
        attn_mask = torch.zeros(20, 20)
        attention_weights = torch.softmax((((query @ key.transpose((- 2), (- 1))) / query.size((- 1))) + attn_mask), dim=(- 1))
        attention_weights = self.dropout(attention_weights)
        x1 = torch.einsum('bij,bjk->bik', attention_weights, v1)
        x2 = self.qkv(x1)
        x3 = ((x2[:, (0 * emb_dim)] + x2[:, (1 * emb_dim)]) + x2[:, (2 * emb_dim)])
        return x3



emb_dim = 1
num_heads = 1
func = Model(16, 2).to('cuda')



x = torch.rand(31, 33)


test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (31x33 and 16x48)

jit:
Failed running call_module L__self___qkv(*(FakeTensor(..., device='cuda:0', size=(31, 33)),), **{}):
a and b must have same reduction dim, but got [31, 33] X [16, 48].

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''