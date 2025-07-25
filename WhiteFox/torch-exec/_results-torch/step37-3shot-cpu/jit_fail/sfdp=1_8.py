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

    def __init__(self, d_model, n_heads, dropout_p):
        super().__init__()
        self.d_model = d_model
        self.n_heads = n_heads
        self.dropout_p = dropout_p
        d_qkv = d_model // n_heads
        self.qkv_conv = torch.nn.Conv2d(d_model, 3 * d_qkv, 1, stride=1, padding=1)
        self.output_conv = torch.nn.Conv2d(d_qkv, d_model, 1, stride=1, padding=0)

    def forward(self, x1, x2, x3):
        qkv = self.qkv_conv(x1)
        (b, c, h, w) = qkv.shape
        qkv = qkv.view(b, 3, self.n_heads, c // self.n_heads, h * w)[0].permute(2, 3, 0, 1)
        (query, key, value) = torch.chunk(qkv, 3, dim=-1)
        inv_denom = 1.0 / math.sqrt(math.sqrt(self.d_model))
        scaled_qk = torch.matmul(query, key.transpose(-2, -1)).div(inv_denom)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = torch.matmul(dropout_qk, value)
        output_head = output.transpose(1, 2).contiguous().view(b, self.d_model, h, w).unsqueeze(0)
        output = self.output_conv(output_head)
        return (output, query, value, softmax_qk, dropout_qk, scaled_qk)


d_model = 256
n_heads = 8
dropout_p = 0.1
func = Model(d_model, n_heads, dropout_p).to('cpu')


d_model = 256
x1 = torch.randn(1, d_model, 64, 64)

d_model = 256
x2 = torch.randn(1, d_model, 64, 64)

d_model = 256
x3 = torch.randn(1, d_model, 64, 64)

test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
shape '[1, 3, 8, 12, 4356]' is invalid for input of size 418176

jit:
Failed running call_method view(*(FakeTensor(..., size=(1, 96, 66, 66)), 1, 3, 8, 12, 4356), **{}):
shape '[1, 3, 8, 12, 4356]' is invalid for input of size 418176

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''