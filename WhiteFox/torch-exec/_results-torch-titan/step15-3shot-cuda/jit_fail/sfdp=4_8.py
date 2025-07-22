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

    def __init__(self, hidden_size):
        super().__init__()
        self.hidden_size = hidden_size
        self.matmul1 = torch.nn.Linear((3 * hidden_size), hidden_size, bias=False)
        self.matmul2 = torch.nn.Linear(hidden_size, 1)

    def transpose_for_scores(self, x):
        new_x_shape = (x.size()[:(- 1)] + (self.num_attention_heads, self.attention_head_size))
        x = x.view(*new_x_shape)
        return x.permute(0, 2, 1, 3)

    def forward(self, query, key, value, mask):
        self.num_attention_heads = 2
        self.attention_head_size = 16
        q = self.matmul1(query)
        k = self.matmul1(key)
        v = self.matmul1(value)
        q = self.transpose_for_scores(q)
        k = self.transpose_for_scores(k)
        v = self.transpose_for_scores(v)
        qk = ((q @ k.transpose((- 2), (- 1))) / math.sqrt(q.size((- 1))))
        qk = (qk + mask)
        attn_weight = torch.softmax(qk, dim=(- 1))
        output = (attn_weight @ v)
        return (output, attn_weight)



hidden_size = 1
func = Model(23).to('cuda')



query = torch.randn(2, 6, 3, 23)



key = torch.randn(2, 7, 3, 23)



value = torch.randn(2, 7, 3, 23)



query = torch.randn(2, 6, 3, 23)


mask = torch.zeros_like(query)


test_inputs = [query, key, value, mask]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (36x23 and 69x23)

jit:
Failed running call_module L__self___matmul1(*(FakeTensor(..., device='cuda:0', size=(2, 6, 3, 23)),), **{}):
a and b must have same reduction dim, but got [36, 23] X [69, 23].

from user code:
   File "<string>", line 31, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''