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

    def __init__(self, attention_dim, num_attn_heads, dropout_p):
        super().__init__()
        w_init_range = 0.1
        self.projection_dim = attention_dim * num_attn_heads
        self.query = torch.nn.Linear(self.projection_dim, self.projection_dim, bias=False)
        self.key = torch.nn.Linear(self.projection_dim, self.projection_dim, bias=False)
        self.value = torch.nn.Linear(self.projection_dim, self.projection_dim, bias=False)
        self.output = torch.nn.Linear(self.projection_dim, self.projection_dim, bias=False)
        self.softmax = torch.nn.Softmax(dim=-1)
        self.dropout = torch.nn.Dropout(dropout_p)
        torch.nn.init.normal_(self.key.weight, std=w_init_range)
        torch.nn.init.normal_(self.query.weight, std=w_init_range)
        torch.nn.init.normal_(self.value.weight, std=w_init_range)
        torch.nn.init.normal_(self.output.weight, std=w_init_range)

    def forward(self, query, key, value, mask):
        q = self.query(query).view(-1, self.num_attn_heads, self.attention_dim).permute(1, 0, 2)
        k = self.key(key).view(-1, self.num_attn_heads, self.attention_dim).permute(1, 0, 2)
        v = self.value(value).view(-1, self.num_attn_heads, self.attention_dim).permute(1, 0, 2)
        q = kq = torch.nn.functional.dropout(q, p=dropout_p, training=self.training)
        v = kv = torch.nn.functional.dropout(v, p=dropout_p, training=self.training)
        scores_per_head = torch.matmul(q, k.transpose(-2, -1)).mul(self.scale_factor)
        scores_per_head = self.softmax(scores_per_head)
        output_per_head = torch.matmul(scores_per_head, kv).permute(1, 0, 2)
        final_output = self.output(output_per_head.flatten(1))
        return final_output


attention_dim = 1
num_attn_heads = 1
dropout_p = 1

func = Model(attention_dim, num_attn_heads, dropout_p).to('cpu')


query = torch.randn(1, 1280)

key = torch.randn(2, 1280)

value = torch.randn(2, 1280)

mask = torch.zeros(1, 2).long()

test_inputs = [query, key, value, mask]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x1280 and 1x1)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 1280)), Parameter(FakeTensor(..., size=(1, 1), requires_grad=True)), None), **{}):
a and b must have same reduction dim, but got [1, 1280] X [1, 1].

from user code:
   File "<string>", line 31, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''