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

    def __init__(self, channels=256, heads=8, n=64, dropout_p=0.1, use_bias=True):
        super().__init__()
        self.channels = channels
        self.heads = heads
        self.to_qkv = torch.nn.Conv2d(channels, (3 * channels), 1, stride=1, padding=0, bias=use_bias)
        self.to_out = torch.nn.Conv2d(channels, channels, 1, stride=1, padding=0, bias=use_bias)
        self.w_q = torch.nn.Linear(channels, n)
        self.w_k = torch.nn.Linear(channels, n)
        self.w_v = torch.nn.Linear(channels, n)
        self.dropout = torch.nn.Dropout(p=dropout_p)

    def forward(self, x):
        (b, c, h, w) = x.shape
        qkv = self.to_qkv(x)
        (q, k, v) = tuple(rearrange(qkv, 'b (qkv heads c) h w -> qkv b heads c (h w)', heads=self.heads, qkv=3, h=h, w=w))
        q = self.w_q(q)
        k = self.w_k(k)
        v = self.w_v(v)
        dot = torch.matmul(q, k.transpose((- 2), (- 1)))
        inv_scale_factor = (1.0 / math.sqrt(math.sqrt(q.shape[(- 1)])))
        scaled_dot = (dot * inv_scale_factor)
        softmax = torch.softmax(scaled_dot, dim=(- 1))
        softmax_dropout = self.dropout(softmax)
        out = torch.matmul(softmax_dropout, v)
        out = rearrange(out, 'b heads c (h w) -> b (heads c) h w', heads=self.heads, h=h, w=w)
        return self.to_out(out)



func = Model().to('cuda')



x = torch.randn(4, 256, 64, 64)


test_inputs = [x]

# JIT_FAIL
'''
direct:
name 'rearrange' is not defined

jit:
name 'rearrange' is not defined

from user code:
   File "<string>", line 31, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''