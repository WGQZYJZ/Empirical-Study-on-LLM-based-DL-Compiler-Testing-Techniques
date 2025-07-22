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

    def __init__(self, dropout_p, query_emb_dim, content_emb_dim, out_emb_dim):
        super().__init__()
        self.dropout_p = dropout_p
        self.query = torch.nn.Parameter(torch.empty((query_emb_dim,)))
        self.key = torch.nn.Parameter(torch.empty((content_emb_dim, query_emb_dim)))
        self.value = torch.nn.Parameter(torch.empty((content_emb_dim,)))
        self.fc = torch.nn.Linear(self.value.shape[0], out_emb_dim, bias=False)
        self.scale_factor = self.key.shape[0] ** (-0.5)

    def forward(self, q, contents):
        qk = torch.matmul(q, self.key.transpose(-2, -1))
        v = self.fc(self.value)
        scaled_qk = qk * self.scale_factor
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = dropout_qk.matmul(v)
        return output


dropout_p = 1
query_emb_dim = 1
content_emb_dim = 1
out_emb_dim = 1

func = Model(dropout_p, query_emb_dim, content_emb_dim, out_emb_dim).to('cpu')


q = torch.randn(8, 16)

contents = torch.randn(117, 8, 64)

test_inputs = [q, contents]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (8x16 and 1x1)

jit:
Failed running call_function <built-in method matmul of type object at 0x7ed373d96ec0>(*(FakeTensor(..., size=(8, 16)), FakeTensor(..., size=(1, 1), requires_grad=True)), **{}):
a and b must have same reduction dim, but got [8, 16] X [1, 1].

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''