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

    def __init__(self, nhead, d_model, dropout=0.0, bias=True):
        super().__init__()
        self.nhead = nhead
        self.dim = d_model
        self.dropout = dropout
        self.head_dim = (d_model // nhead)
        self.q_linear = torch.nn.Linear(self.dim, self.dim, bias=bias)
        self.k_linear = torch.nn.Linear(self.dim, self.dim, bias=bias)
        self.v_linear = torch.nn.Linear(self.dim, self.dim, bias=bias)
        self.out_linear = torch.nn.Linear(self.dim, self.dim)

    def forward(self, q, k, v, mask=None):
        bs = q.size(0)
        q = self.q_linear(q).view(bs, (- 1), self.nhead, self.head_dim).transpose(1, 2)
        k = self.k_linear(k).view(bs, (- 1), self.nhead, self.head_dim).transpose(1, 2)
        v = self.v_linear(v).view(bs, (- 1), self.nhead, self.head_dim).transpose(1, 2)
        if (mask is not None):
            attn_mask = (mask == 0).view(bs, 1, 1, (- 1)).repeat(1, self.nhead, (self.dim // self.nhead), 1)
            attn_mask = torch.where(attn_mask, (torch.ones_like(attn_mask) * float('-inf')), attn_mask)
            q = torch.where(attn_mask.bool(), torch.zeros_like(q), q)
            k = torch.where(attn_mask.bool(), torch.zeros_like(k), k)
        scale = (1.0 / math.sqrt((self.dim // self.nhead)))
        qk = (torch.matmul(q, k.transpose(2, 3)) * scale)
        attn_weight = torch.softmax(qk, dim=3)
        if (self.dropout > 0):
            attn_weight = F.dropout(attn_weight, p=self.dropout, training=self.training)
        output = torch.matmul(attn_weight, v)
        output = output.transpose(1, 2).contiguous().view(bs, (- 1), self.dim)
        if (self.dropout > 0):
            output = F.dropout(output, p=self.dropout, training=self.training)
        output = (output * (self.dim ** (- 0.5)))
        output = self.out_linear(output)
        return output



nhead = 1
d_model = 1
func = MultiHeadAttention(2, 64).to('cuda')



x1 = torch.randn(1, 10, 64)



x2 = torch.randn(1, 16, 64)



x3 = torch.randn(1, 16, 64)



mask = torch.tensor([[0, 1, 1, 1, 1, 1, 1, 1, 1, 1]])


test_inputs = [x1, x2, x3, mask]

# JIT_FAIL
'''
direct:
The size of tensor a (10) must match the size of tensor b (32) at non-singleton dimension 3

jit:
Failed running call_function <built-in method where of type object at 0x7f5c5fc699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 2, 32, 10), dtype=torch.bool), FakeTensor(..., device='cuda:0', size=(1, 2, 10, 32)), FakeTensor(..., device='cuda:0', size=(1, 2, 10, 32))), **{}):
Attempting to broadcast a dimension of length 32 at -1! Mismatching argument at index 1 had torch.Size([1, 2, 10, 32]); but expected shape should be broadcastable to [1, 2, 32, 10]

from user code:
   File "<string>", line 36, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''