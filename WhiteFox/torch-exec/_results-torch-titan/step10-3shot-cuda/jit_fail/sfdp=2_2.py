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

    def __init__(self, dim, num_heads, head_dim, dropout_p):
        super().__init__()
        self.w_q = torch.nn.Linear(dim, (num_heads * head_dim))
        self.w_k = torch.nn.Linear(dim, (num_heads * head_dim))
        self.w_v = torch.nn.Linear(dim, (num_heads * head_dim))
        self.w_o = torch.nn.Linear((num_heads * head_dim), dim)
        self.dropout_p = dropout_p
        self.num_heads = num_heads
        self.head_dim = head_dim
        self.scaling = (self.head_dim ** (- 0.5))

    def forward(self, x):
        q = self.w_q(x)
        k = self.w_k(x)
        v = self.w_v(x)
        q = q.reshape([q.shape[0], q.shape[1], self.num_heads, self.head_dim])
        k = k.reshape([k.shape[0], k.shape[1], self.num_heads, self.head_dim])
        v = v.reshape([v.shape[0], v.shape[1], self.num_heads, self.head_dim])
        q *= self.scaling
        q = q.transpose(1, 2)
        k = k.transpose(1, 2)
        v = v.transpose(1, 2)
        k = k.transpose((- 2), (- 1))
        attn_score = (q @ k)
        attn_p = torch.nn.functional.dropout(attn_score.softmax(dim=(- 1)), p=self.dropout_p)
        attn_output = (attn_p @ v)
        attn_output = attn_output.transpose(1, 2)
        attn_output = attn_output.reshape([attn_output.shape[0], (- 1), (self.num_heads * self.head_dim)])
        return self.w_o(attn_output)



dim = 1
num_heads = 1
head_dim = 1
dropout_p = 1

func = Model(dim, num_heads, head_dim, dropout_p).to('cuda')



x = torch.randn(64, 16, 64)


test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1024x64 and 1x1)

jit:
Failed running call_module L__self___w_q(*(FakeTensor(..., device='cuda:0', size=(64, 16, 64)),), **{}):
a and b must have same reduction dim, but got [1024, 64] X [1, 1].

from user code:
   File "<string>", line 29, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''