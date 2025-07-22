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

class MultiHeadAttention(nn.Module):

    def __init__(self, model_dim, num_heads):
        super().__init__()
        self.head_dim = model_dim // num_heads
        self.num_heads = num_heads
        w_linear = lambda d, s, i: nn.Linear(d, s, bias=False)
        self.query = w_linear(model_dim, model_dim, 'query')
        self.key = w_linear(model_dim, model_dim, 'key')
        self.value = w_linear(model_dim, model_dim, 'value')
        self.out = w_linear(model_dim, model_dim, 'output')

    def _scaled_dot_product(self, query, key):
        return torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(self.head_dim)

    def forward(self, x, mask=None, attn_mask=None):
        b = x.shape[0]
        residual = x
        batch_size = x.shape[0]
        num_heads = self.num_heads
        head_dim = self.head_dim
        input_x = torch.cat([self.query(x).reshape(b, num_heads, -1), self.key(x).reshape(b, num_heads, -1), self.value(x).reshape(b, num_heads, -1)], dim=-1)
        input_x = input_x.reshape((batch_size * num_heads, -1, head_dim))
        qk = self._scaled_dot_product(input_x[:, :, :], input_x)
        qk = qk.reshape((batch_size, num_heads, -1, input_x.size(-1)))
        qk_softmax = torch.softmax(qk, dim=-1)
        qk_softmax = torch.dropout(qk_softmax, 0.2, train=True)
        output = torch.matmul(qk, input_x)
        if len(output.shape) == 3:
            output = output.permute(0, 2, 1, 3).contiguous()
            output = output.reshape((batch_size, -1, head_dim * num_heads))
        else:
            output = output.reshape((batch_size, -1, head_dim * num_heads))
        output = self.out(output)
        output = output + residual
        return output

class Model(torch.nn.Module):

    def __init__(self, model_dim, num_heads):
        super().__init__()
        self.mha = MultiHeadAttention(model_dim, num_heads)

    def forward(self, x, mask, attn_mask):
        return self.mha(x, mask, attn_mask)


model_dim = 1
num_heads = 1

func = Model(model_dim, num_heads).to('cpu')


x = torch.randn(16, 32, 64)

mask = torch.arange(0, 32).expand(16, 32)
attn_mask = 1

test_inputs = [x, mask, attn_mask]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (512x64 and 1x1)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(16, 32, 64)), Parameter(FakeTensor(..., size=(1, 1), requires_grad=True)), None), **{}):
a and b must have same reduction dim, but got [512, 64] X [1, 1].

from user code:
   File "<string>", line 57, in forward
  File "<string>", line 34, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''