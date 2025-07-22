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

class SelfAttention(torch.nn.Module):

    def __init__(self, dim_in, dim_out, heads, dropout):
        super().__init__()
        self.dim_out = dim_out
        self.heads = heads
        self.scale_factor = dim_out // heads
        self.to_q = torch.nn.Linear(dim_in, dim_out, bias=False)
        self.to_k = torch.nn.Linear(dim_in, dim_out, bias=False)
        self.to_v = torch.nn.Linear(dim_in, dim_out, bias=False)
        self.to_out = torch.nn.Linear(dim_out, dim_out)
        self.dropout = torch.nn.Dropout(dropout)

    def forward(self, x):
        num_heads = self.heads
        b = x.shape[0]
        _ = x.shape[-1]
        q = self.to_q(x).softmax(-1).unsqueeze(-3)
        k = self.to_k(x).softmax(-2).transpose(-2, -1).unsqueeze(-3)
        v = self.to_v(x).transpose(-2, -1).unsqueeze(-3)
        q = torch.cat(torch.unbind(q, dim=-3), dim=-2)
        k = torch.cat(torch.unbind(k, dim=-3), dim=-2)
        v = torch.cat(torch.unbind(v, dim=-3), dim=-2)
        output = self.dropout(torch.matmul(q, v.transpose(-2, -1)) / math.sqrt(self.scale_factor))
        output = torch.matmul(output, k)
        output = output.apply(lambda x: x / x.shape[-1])
        y = torch.cat(torch.unbind(output, dim=-3), dim=-1)
        return self.to_out(y)


dim_in = 1
dim_out = 1
heads = 1
dropout = 1
func = SelfAttention(16, 64, num_heads, 0.2).to('cpu')


x = torch.randn(2, 128, 16)

test_inputs = [x]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [2, 64] but got: [2, 128].

jit:
Failed running call_function <built-in method matmul of type object at 0x776853596ec0>(*(FakeTensor(..., size=(2, 128, 64)), FakeTensor(..., size=(2, 128, 64))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [2, 64] but got: [2, 128].

from user code:
   File "<string>", line 36, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''