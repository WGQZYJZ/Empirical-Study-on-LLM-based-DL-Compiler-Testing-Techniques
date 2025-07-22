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

    def __init__(self, dim, num_heads=8):
        super().__init__()
        self.dim = dim
        self.num_heads = num_heads
        self.scale_factor = math.sqrt(self.dim)
        self.w_q = torch.nn.Linear(dim, dim * num_heads, bias=False)
        self.w_k = torch.nn.Linear(dim, dim * num_heads, bias=False)
        self.w_v = torch.nn.Linear(dim, dim * num_heads, bias=False)

    def forward(self, x1, x2):
        q = self.w_q(x1)
        k = self.w_k(x2)
        v = self.w_v(x1)
        q = self._reshape(q, x2.size(0))
        k = self._reshape(k, x1.size(0))
        v = self._reshape(v, x1.size(0))
        scale_factor = self.scale_factor
        inv_scale_factor = 1 / scale_factor
        dropout_p = 0.1
        return torch.nn.functional.dropout(torch.softmax(torch.matmul(q, k.transpose(-2, -1)).div(inv_scale_factor), dim=-1), p=dropout_p).matmul(v)

    def _reshape(self, x, batch_size):
        dim = x.size(-1)
        splitted = torch.split(x, split_size_or_sections=self.num_heads, dim=-1)
        return torch.cat([tensor.view(batch_size, dim, 1, 1) for tensor in splitted], dim=2).view(-1, dim)


dim = 1

func = Model(dim).to('cpu')


x1 = torch.randn(100, 256)

x2 = torch.randn(100, 256)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (100x256 and 1x8)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(100, 256)), Parameter(FakeTensor(..., size=(8, 1), requires_grad=True)), None), **{}):
a and b must have same reduction dim, but got [100, 256] X [1, 8].

from user code:
   File "<string>", line 25, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''