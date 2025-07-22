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

    def __init__(self, query_hidden_size, key_hidden_size, num_heads, size_per_head):
        super().__init__()
        self.size_per_head = size_per_head
        self.num_heads = num_heads
        self.query_projection = torch.nn.Linear(query_hidden_size, num_heads * size_per_head, bias=False)
        self.key_projection = torch.nn.Linear(key_hidden_size, num_heads * size_per_head, bias=False)
        self.value_projection = torch.nn.Linear(size_per_head, num_heads * size_per_head, bias=False)
        self.output_projection = torch.nn.Linear(num_heads * size_per_head, size_per_head, bias=False)

    def transpose_for_scores(self, input_tensor, batch_size):
        tensor = input_tensor.view(batch_size, -1, self.num_heads, self.size_per_head)
        tensor = tensor.transpose(1, 2).contiguous().view(batch_size * self.num_heads, -1, self.size_per_head)
        return tensor

    def forward(self, query, key, value, attention_mask):
        batch_size = query.size(0)
        query = self.query_projection(query)
        key = self.key_projection(key)
        value = self.value_projection(value)
        query = self.transpose_for_scores(query, batch_size)
        key = self.transpose_for_scores(key, batch_size)
        value = self.transpose_for_scores(value, batch_size)
        attention_mask = attention_mask.view(batch_size * self.num_heads, 1, 1, -1)
        attention_mask = (1.0 - attention_mask) * float('-inf')
        attention_mask = attention_mask.expand(batch_size * self.num_heads, 1, -1, -1)
        attention_mask = attention_mask.contiguous().view(batch_size * self.num_heads, 1, 1, -1)
        context = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        context = context + attention_mask
        context = torch.softmax(context, dim=-1)
        output = context @ value
        output = output.transpose(1, 2)
        output = output.reshape(batch_size, -1, output.size(2))
        output = output.transpose(0, 1)
        output = self.output_projection(output)
        return output


query_hidden_size = 1
key_hidden_size = 1
num_heads = 1
size_per_head = 1

func = Model(query_hidden_size, key_hidden_size, num_heads, size_per_head).to('cpu')

params = [32, 32, 2, 8]


query = torch.autograd.Variable(torch.randn(1, 2, params[0]), requires_grad=True)
params = [32, 32, 2, 8]


key = torch.autograd.Variable(torch.randn(1, 2, params[1]), requires_grad=True)
params = [32, 32, 2, 8]
params = [32, 32, 2, 8]


value = torch.autograd.Variable(torch.randn(1, 2, params[2], params[3]), requires_grad=True)
attention_mask = 1

test_inputs = [query, key, value, attention_mask]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (2x32 and 1x1)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 2, 32)), Parameter(FakeTensor(..., size=(1, 1), requires_grad=True)), None), **{}):
a and b must have same reduction dim, but got [2, 32] X [1, 1].

from user code:
   File "<string>", line 31, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''