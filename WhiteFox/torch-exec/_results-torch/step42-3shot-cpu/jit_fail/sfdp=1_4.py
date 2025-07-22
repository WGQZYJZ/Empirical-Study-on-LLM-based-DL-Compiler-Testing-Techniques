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

    def __init__(self, num_heads):
        super().__init__()
        self.query = torch.nn.Linear(3, 4)
        self.key = torch.nn.Linear(3, 4)
        self.value = torch.nn.Linear(3, 4)
        self.num_heads = num_heads
        self.input_len = 3
        self.key_len = 4
        self.value_len = 4
        self.scale_factor = self.key_len ** (-0.5)

    def forward(self, inp):
        vq = self.query(inp).reshape(self.num_heads, self.input_len // self.num_heads, self.key_len)
        vk = self.key(inp).reshape(self.num_heads, self.key_len, self.key_len)
        vv = self.value(inp).reshape(self.num_heads, self.input_len // self.num_heads, self.value_len)
        qk = torch.matmul(vq, vk.transpose(-2, -1))
        dk = self.key_len ** (-0.5)
        softmax_qk = qk.div(self.scale_factor).softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.2)
        output = dropout_qk.matmul(vv)
        return output


num_heads = 1

func = Model(num_heads).to('cpu')


x1 = torch.randn(20, 2, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (40x64 and 3x4)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(20, 2, 64)), Parameter(FakeTensor(..., size=(4, 3), requires_grad=True)), Parameter(FakeTensor(..., size=(4,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [40, 64] X [3, 4].

from user code:
   File "<string>", line 27, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''