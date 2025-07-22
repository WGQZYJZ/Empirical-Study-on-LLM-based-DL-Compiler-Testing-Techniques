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

    def __init__(self, d_model, n_heads, d_qkv, scale_attn_weights=False, dropout_p=0.0, attn_mask_mode='add'):
        super().__init__()
        self.linear_q = torch.nn.Linear(d_model, n_heads * d_qkv)
        self.linear_k = torch.nn.Linear(d_model, n_heads * d_qkv)
        self.linear_v = torch.nn.Linear(d_model, n_heads * d_qkv)
        self.scale_attn_weights = scale_attn_weights
        self.dropout = torch.nn.Dropout(p=dropout_p)
        self.attn_mask_mode = attn_mask_mode
        self.sqrt_dk = np.sqrt(d_qkv)

    def forward(self, x1, x2):
        q = self.linear_q(x1)
        k = self.linear_k(x2)
        v = self.linear_v(x2)
        q = q.reshape(*q.shape[:-1], -1, q.shape[-1])
        k = k.reshape(*k.shape[:-1], -1, k.shape[-1])
        v = v.reshape(*v.shape[:-1], -1, v.shape[-1])
        attn = torch.matmul(q, k.transpose(2, 3))
        if self.scale_attn_weights:
            attn = attn / self.sqrt_dk
        if self.attn_mask_mode == 'add':
            attn = attn + attn_mask
        if self.attn_mask_mode == 'mul':
            attn = attn * attn_mask
        attn = attn.softmax(dim=-1)
        attn = self.dropout(attn)
        attn = torch.matmul(attn, v)
        attn = attn.flatten(2, 3)
        return attn


d_model = 1
n_heads = 1
d_qkv = 1

func = Model(d_model, n_heads, d_qkv).to('cpu')


x1 = torch.randn(1, 16, 256)

x2 = torch.randn(2, 16, 256)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (16x256 and 1x1)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 16, 256)), Parameter(FakeTensor(..., size=(1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(1,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [16, 256] X [1, 1].

from user code:
   File "<string>", line 26, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''