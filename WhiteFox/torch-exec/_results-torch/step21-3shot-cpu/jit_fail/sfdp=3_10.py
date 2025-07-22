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

    def __init__(self, dim, input_dim, n_heads):
        super().__init__()
        self.query = torch.nn.Parameter(torch.randn(n_heads, dim, input_dim))
        self.key = torch.nn.Parameter(torch.randn(n_heads, dim, input_dim))
        self.value = torch.nn.Parameter(torch.randn(n_heads, dim, input_dim))
        self.dropout = torch.nn.Dropout(p=0.7)

    def forward(self, x):
        qk = torch.matmul(x, self.key.transpose(-2, -1))
        scaled_qk = qk * int(x.shape[-1]) ** (-0.5)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = self.dropout(softmax_qk)
        output = dropout_qk.matmul(self.value)
        return output


dim = 1
input_dim = 1
n_heads = 1

func = Model(dim, input_dim, n_heads).to('cpu')


x = torch.randn(4, 8, 512)

test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (32x512 and 1x1)

jit:
Failed running call_function <built-in method matmul of type object at 0x719ca6596ec0>(*(FakeTensor(..., size=(4, 8, 512)), FakeTensor(..., size=(1, 1, 1), requires_grad=True)), **{}):
a and b must have same reduction dim, but got [32, 512] X [1, 1].

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''