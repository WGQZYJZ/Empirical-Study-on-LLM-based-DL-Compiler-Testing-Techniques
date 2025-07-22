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



class Model1(torch.nn.Module):

    def __init__(self, d_model=768, nhead=12, dropout_p=0.3):
        super().__init__()
        self.d_model = d_model
        self.nhead = nhead
        self.attn_dropout = dropout_p
        self.q_linear = torch.nn.Linear(d_model, d_model)
        self.k_linear = torch.nn.Linear(d_model, d_model)
        self.v_linear = torch.nn.Linear(d_model, d_model)
        self.out_linear = torch.nn.Linear(d_model, d_model)

    def forward(self, query, key, value, inv_scale_factor):
        (bs, num, _) = key.size()
        q = self.q_linear(query).view(bs, num, self.nhead, (self.d_model // self.nhead)).permute(2, 0, 1, 3)
        k = self.k_linear(key).view(bs, num, self.nhead, (self.d_model // self.nhead)).permute(2, 0, 1, 3)
        v = self.v_linear(value).view(bs, num, self.nhead, (self.d_model // self.nhead)).permute(2, 0, 1, 3)
        q /= inv_scale_factor
        q = q.softmax(dim=(- 1))
        q = torch.nn.functional.dropout(q, self.attn_dropout)
        o = torch.matmul(q, v).permute(0, 2, 1, 3).contiguous().view(bs, num, self.d_model)
        return self.out_linear(o)



func = Model1(d_model=768).to('cuda')



query = torch.randn(5, 86, 768)



key = torch.randn(5, 128, 768)



value = torch.randn(5, 128, 768)

inv_scale_factor = 1

test_inputs = [query, key, value, inv_scale_factor]

# JIT_FAIL
'''
direct:
shape '[5, 128, 12, 64]' is invalid for input of size 330240

jit:
Failed running call_method view(*(FakeTensor(..., device='cuda:0', size=(5, 86, 768)), 5, 128, 12, 64), **{}):
shape '[5, 128, 12, 64]' is invalid for input of size 330240

from user code:
   File "<string>", line 29, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''