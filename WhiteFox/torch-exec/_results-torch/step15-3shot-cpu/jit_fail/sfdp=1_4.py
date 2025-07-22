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

    def __init__(self, key_dim, num_heads, dropout_p=0.1):
        super(Model, self).__init__()
        self.key_dim = key_dim
        self.num_heads = num_heads
        self.dropout_p = dropout_p
        self.qkv = torch.nn.Conv2d(3, 3 * 3 * num_heads, 1, stride=1, padding=1)
        self.o = torch.nn.Conv2d(3 * num_heads, 3, 1, stride=1, padding=1)
        self.scale_factor = math.sqrt(key_dim)

    def forward(self, x):
        x = self.qkv(x)
        (query, key, value) = x.split([3 * self.num_heads, 3 * self.num_heads, 3 * self.num_heads], dim=1)
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk.div(self.scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = torch.matmul(dropout_qk, value)
        return self.o(output.view(-1, 3 * self.num_heads, x.shape[2], x.shape[3])).view(-1, 3, x.shape[2], x.shape[3])


key_dim = 1
num_heads = 1

func = Model(key_dim, num_heads).to('cpu')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
shape '[-1, 3, 66, 66]' is invalid for input of size 13872

jit:
Failed running call_method view(*(FakeTensor(..., size=(1, 3, 68, 68)), -1, 3, 66, 66), **{}):
shape '[-1, 3, 66, 66]' is invalid for input of size 13872

from user code:
   File "<string>", line 32, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''