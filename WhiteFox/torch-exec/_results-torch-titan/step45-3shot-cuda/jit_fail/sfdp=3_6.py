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

    def __init__(self):
        super().__init__()
        self.embed = nn.Linear(768, 384)
        self.layernorm1 = nn.LayerNorm(384, eps=1e-12)
        self.layernorm2 = nn.LayerNorm(768, eps=1e-12)
        self.linear1 = nn.Linear(384, 768)
        self.linear2 = nn.Linear(768, 3072)
        self.dropout = nn.Dropout(0.1)

    def forward(self, query, key, vl):
        q = self.embed(query)
        k = self.embed(key)
        v = self.embed(vl)
        q = self.layernorm1(q)
        k = self.layernorm1(k)
        v = self.layernorm1(v)
        qkv = torch.einsum('bnij,bmij->bnmi', q, k)
        qkv = self.linear2(qkv)
        qkv += (q.unsqueeze(2) + k.unsqueeze(1))
        qkv = (qkv * float(np.sqrt((1.0 / 385))))
        qkv = torch.matmul(qkv, v.transpose(2, 1))
        q = q.matmul(qkv.transpose(2, 3))
        k = torch.matmul(qkv, k.transpose(2, 1))
        v = torch.matmul(qkv, v.transpose(2, 1))
        qkv = torch.cat([q, k, v], dim=2)
        qkv = (qkv + self.linear1(qkv))
        return self.dropout(qkv)



func = Model().to('cuda')



x1 = torch.randn(5, 384, 768)



x2 = torch.randn(5, 384, 768)



x3 = torch.randn(5, 384, 768)


test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
einsum(): the number of subscripts in the equation (4) does not match the number of dimensions (3) for operand 0 and no ellipsis was given

jit:
Failed running call_function <function einsum at 0x7a5599870160>(*('bnij,bmij->bnmi', FakeTensor(..., device='cuda:0', size=(5, 384, 384)), FakeTensor(..., device='cuda:0', size=(5, 384, 384))), **{}):
einsum(): the number of subscripts in the equation (4) does not match the number of dimensions (3) for operand 0 and no ellipsis was given

from user code:
   File "<string>", line 33, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''