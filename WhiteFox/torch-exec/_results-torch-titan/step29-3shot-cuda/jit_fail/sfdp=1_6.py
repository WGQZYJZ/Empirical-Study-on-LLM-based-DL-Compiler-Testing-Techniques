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

    def __init__(self, hidden_size, num_attention_heads, dropout_p=0.5):
        super().__init__()
        self.hidden_dim = hidden_size
        self.num_attention_heads = num_attention_heads
        self.attention_head_size = (hidden_size // num_attention_heads)
        self.all_head_size = (self.num_attention_heads * self.attention_head_size)
        self.query = torch.nn.Linear(hidden_size, self.all_head_size)
        self.key = torch.nn.Linear(hidden_size, self.all_head_size)
        self.value = torch.nn.Linear(hidden_size, self.all_head_size)
        self.dropout = torch.nn.Dropout(p=dropout_p)

    def transpose_for_scores(self, q, k, v):
        new_q_shape = (q.size()[:(- 1)] + (self.num_attention_heads, self.attention_head_size))
        q = q.view(*new_q_shape)
        k = k.view(*new_q_shape)
        v = v.view(*new_q_shape)
        return (q, k, v)

    def forward(self, x1, x2):
        q = self.query(x1)
        k = self.key(x1)
        v = self.value(x2)
        (q, k, v) = self.transpose_for_scores(q, k, v)
        output = torch.matmul(q, k.transpose((- 2), (- 1)))
        output = output.softmax(dim=(- 1))
        output = self.dropout(output)
        output = torch.matmul(output, v)
        output = output.view(*output.size()[:(- 2)], output.size((- 2)), self.hidden_dim)
        return output



hidden_size = 1
num_attention_heads = 1

func = Model(hidden_size, num_attention_heads).to('cuda')



x1 = torch.randn(2, 10, 12)



x2 = torch.randn(2, 15, 12)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (20x12 and 1x1)

jit:
Failed running call_module L__self___query(*(FakeTensor(..., device='cuda:0', size=(2, 10, 12)),), **{}):
a and b must have same reduction dim, but got [20, 12] X [1, 1].

from user code:
   File "<string>", line 36, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''