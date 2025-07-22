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

    def __init__(self, dim=64, h=8, dropout_p=0.2):
        super().__init__()
        self.dim = dim
        self.head = h
        self.dk = dim // h
        self.scale_factor = self.dk ** (-0.5)
        self.query = torch.nn.Parameter(torch.randn(dim, dim))
        self.key = torch.nn.Parameter(torch.randn(dim, dim))
        self.value = torch.nn.Parameter(torch.randn(dim, dim))
        self.proj = torch.nn.Linear(dim * 2, dim * 2)
        self.dropout = torch.nn.Dropout(dropout_p)

    def forward(self, x):
        query = self.query.unsqueeze(1)
        key = self.key.transpose(-2, -1).unsqueeze(1)
        value = self.value.unsqueeze(1)
        batch = x.size(0)
        qk = torch.matmul(query, key)
        scaled_qk = qk * self.scale_factor
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = self.dropout(softmax_qk)
        qkv = torch.matmul(dropout_qk, value)
        x = qkv.transpose(3, 1)
        x = x.reshape(batch, -1)
        x = self.proj(x)
        x = x.reshape(batch, -1, 2, self.dim)
        x = x.transpose(3, 1)
        output = [x[:, :, 0, :], x[:, :, 1, :]]
        return output


func = Model(dim=64, h=8, dropout_p=0.2).to('cpu')


x = torch.randn(1, 8, 64)

test_inputs = [x]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [64, 64] but got: [64, 1].

jit:
Failed running call_function <built-in method matmul of type object at 0x75a5f4b96ec0>(*(FakeTensor(..., size=(64, 1, 64), requires_grad=True), FakeTensor(..., size=(64, 1, 64), requires_grad=True)), **{}):
Expected size for first two dimensions of batch2 tensor to be: [64, 64] but got: [64, 1].

from user code:
   File "<string>", line 32, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''