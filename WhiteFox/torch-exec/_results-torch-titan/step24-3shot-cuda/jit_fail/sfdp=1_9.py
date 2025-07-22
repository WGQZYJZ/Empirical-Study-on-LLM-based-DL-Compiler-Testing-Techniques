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



class ScaledDotProductAttention(torch.nn.Module):

    def __init__(self, dropout_p):
        super().__init__()
        self.dropout_p = dropout_p

    def forward(self, query, key, value, inv_scale_factor):
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = dropout_qk.matmul(value)
        return output




class Model(torch.nn.Module):

    def __init__(self, dropout_p):
        super().__init__()
        self.transformer_block = torch.nn.TransformerEncoderLayer(d_model=64, nhead=8)
        self.attention = ScaledDotProductAttention(dropout_p)

    def forward(self, x1, x2, x3, x4):
        v1 = self.transformer_block(x1)
        v2 = x2.repeat(1, 8, 1, 1)
        v3 = x3.repeat(1, 8, 1, 1)
        v4 = self.attention(query=v1, key=v2, value=v3, inv_scale_factor=(1 / (64 ** 0.5)))
        v5 = (v4 + x4)
        return v5



dropout_p = 1

func = Model(dropout_p).to('cuda')



x1 = torch.randn(1, 64, 64, 64)



x2 = torch.randn(1, 1, 64, 64)



x3 = torch.randn(1, 1, 64, 64)



x4 = torch.randn(1, 8, 64, 64)


test_inputs = [x1, x2, x3, x4]

# JIT_FAIL
'''
direct:
query should be unbatched 2D or batched 3D tensor but received 4-D query tensor

jit:
Failed running call_module L__self___transformer_block(*(FakeTensor(..., device='cuda:0', size=(1, 64, 64, 64)),), **{}):
query should be unbatched 2D or batched 3D tensor but received 4-D query tensor

from user code:
   File "<string>", line 40, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''