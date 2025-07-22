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
        self.qkv_proj = torch.nn.Linear(6, 25, bias=False)

    def forward(self, x1):
        qkv = F.gelu(self.qkv_proj(x1))
        qkv = qkv.split(25, dim=(- 1))
        q = qkv[0]
        k = qkv[1]
        v = qkv[2]
        q = q.unsqueeze(dim=(- 3))
        q = q.expand_as(k)
        scaled_qk = torch.matmul(q, k.transpose_((- 2), (- 1)))
        inv_scale_factor = (1.0 / math.sqrt(math.sqrt(6)))
        scaled_qk = scaled_qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.5)
        output = torch.matmul(dropout_qk, v)
        return output



func = Model().to('cuda')



x1 = torch.randn(1, 6, 4)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (6x4 and 6x25)

jit:
Failed running call_module L__self___qkv_proj(*(FakeTensor(..., device='cuda:0', size=(1, 6, 4)),), **{}):
a and b must have same reduction dim, but got [6, 4] X [6, 25].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''