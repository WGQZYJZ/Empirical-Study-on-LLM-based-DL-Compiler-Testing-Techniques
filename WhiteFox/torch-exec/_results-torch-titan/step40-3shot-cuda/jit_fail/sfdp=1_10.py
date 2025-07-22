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

    def __init__(self, output_dim, n_heads=8):
        super().__init__()
        self.n_heads = n_heads
        self.dim_head = (output_dim / self.n_heads)
        self.qk_v_proj = torch.nn.Linear((output_dim * 2), (output_dim * 3), bias=False)
        self.ff_proj = torch.nn.Linear(output_dim, output_dim)

    def forward(self, inputs, valid_length=None):
        kqv = torch.cat([self.qk_v_proj(inputs).chunk(3, dim=(- 1))], dim=0)
        k = kqv[0]
        q = kqv[1]
        v = kkv[2]
        scale_factor = (1 / (self.dim_head ** 0.5))
        qkp = (torch.matmul(q, k.transpose((- 2), (- 1))) * scale_factor)
        softmax_qkp = torch.nn.functional.softmax(qkp, dim=(- 1))
        dropout_qkp = torch.nn.functional.dropout(softmax_qkp, p=dropout_p)
        output = torch.matmul(dropout_qkp, v)
        return self.ff_proj(output)



output_dim = 1

func = Model(output_dim).to('cuda')



inputs = torch.randn(4, 80, 80)


test_inputs = [inputs]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (320x80 and 2x3)

jit:
Failed running call_module L__self___qk_v_proj(*(FakeTensor(..., device='cuda:0', size=(4, 80, 80)),), **{}):
a and b must have same reduction dim, but got [320, 80] X [2, 3].

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''