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

    def __init__(self, d_model, n_head, d_k, d_v, dropout_p=0.1):
        super(Model, self).__init__()
        self.w_q = torch.nn.Linear(d_model, (n_head * d_k))
        self.w_k = torch.nn.Linear(d_model, (n_head * d_k))
        self.w_v = torch.nn.Linear(d_model, (n_head * d_v))
        self.w_o = torch.nn.Linear((n_head * d_v), d_model)
        self.dropout = torch.nn.Dropout(dropout_p)

    def attention(self, q, k, v, mask=None):
        n_head = self.n_head
        d_k = self.d_k
        d_v = self.d_v
        d_model = q.size((- 1))
        residual = q
        q = self.w_q(q).view(n_head, (- 1), d_k).transpose(1, 2)
        k = self.w_k(k).view(n_head, (- 1), d_k).transpose(1, 2)
        v = self.w_v(v).view(n_head, (- 1), d_v).transpose(1, 2)
        scaled_attention = (torch.matmul(q, k.transpose((- 2), (- 1))) / np.sqrt(d_k).item())
        if (mask is not None):
            mask = mask.unsqueeze(1).expand(mask.size(0), n_head, mask.size(1))
            scaled_attention = scaled_attention.masked_fill_((mask == 0), (- 1e-09))
        attention = self.dropout(torch.nn.functional.softmax(scaled_attention, dim=(- 1)))
        output = torch.matmul(attention, v)
        output = output.transpose(1, 2).contiguous().view(n_head, (- 1), d_model)
        output = self.w_o(output)
        return (output + residual)

    def forward(self, q, k, v, mask=None):
        d_model = q.size((- 1))
        n = q.size(0)
        bsz = q.size(1)
        q = q.view(n, bsz, (- 1))
        k = k.view(n, bsz, (- 1))
        v = v.view(n, bsz, (- 1))
        q = self.w_q(q)
        k = self.w_k(k)
        v = self.w_v(v)
        y = self.attention(q, k, v, mask)
        y = y.view(n, bsz, (- 1))
        y = self.dropout(y)
        return y



d_model = 1
n_head = 1
d_k = 1
d_v = 1

func = Model(d_model, n_head, d_k, d_v).to('cuda')



q = torch.randn(1, 8, 64)



k = torch.randn(1, 4, 64)



v = torch.randn(1, 4, 64)



mask = torch.ByteTensor([1, 0, 0, 1])


test_inputs = [q, k, v, mask]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (8x64 and 1x1)

jit:
Failed running call_module L__self___w_q(*(FakeTensor(..., device='cuda:0', size=(1, 8, 64)),), **{}):
a and b must have same reduction dim, but got [8, 64] X [1, 1].

from user code:
   File "<string>", line 51, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''