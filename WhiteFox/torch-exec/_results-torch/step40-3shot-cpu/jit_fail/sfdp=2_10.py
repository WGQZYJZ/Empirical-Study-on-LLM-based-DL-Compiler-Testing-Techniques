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

    def __init__(self, input_shape, num_heads=1, dropout_p=0.5):
        super().__init__()
        self.num_heads = num_heads
        inner_dim = input_shape[-1]
        self.qkv = torch.nn.Linear(inner_dim, 3 * inner_dim)
        self.dropout_p = dropout_p
        self.scale_factor = torch.sqrt(torch.FloatTensor([inner_dim // num_heads]))

    def forward(self, query, key, value):
        qkv = self.qkv(query).chunk(3, dim=-1)
        (q, k, v) = map(lambda t: rearrange(t, 'b n (h d) -> (b h) n d', h=self.num_heads), qkv)
        qk = torch.matmul(q, k.transpose(-2, -1))
        inv_scale_factor = 1 / self.scale_factor
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = dropout_qk.matmul(v)
        output = rearrange(output, '(b h) n d -> b n (h d)', h=self.num_heads)
        return output


input_shape = 1
func = Model((4, 8), num_heads=2).to('cpu')


query = torch.randn(4, 2)

key = torch.randn(2, 4)

value = torch.randn(2, 4)

test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (4x2 and 8x24)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(4, 2)), Parameter(FakeTensor(..., size=(24, 8), requires_grad=True)), Parameter(FakeTensor(..., size=(24,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [4, 2] X [8, 24].

from user code:
   File "<string>", line 24, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''