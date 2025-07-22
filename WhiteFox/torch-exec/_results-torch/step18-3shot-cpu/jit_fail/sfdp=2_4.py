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

    def __init__(self, input_size, num_heads, dropout=0.05):
        super().__init__()
        self.num_heads = num_heads
        self.head_size = input_size // num_heads
        self.scale_factor = torch.tensor(self.head_size).pow(-0.5)
        self.query = torch.nn.Linear(input_size, input_size)
        self.key = torch.nn.Linear(input_size, input_size)
        self.value = torch.nn.Linear(input_size, input_size)
        self.dropout_p = torch.nn.Parameter(torch.scalar_tensor(dropout))

    def forward(self, x):
        q = self.query(x)
        k = self.key(x)
        v = self.value(x)
        qk = torch.matmul(q, k.transpose(-2, -1))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(v)
        return output

    def generate_config(self):
        self.config = dict(input_size=input_size, num_heads=num_heads, dropout_p=dropout_p.item())


input_size = 1
num_heads = 1

func = Model(input_size, num_heads).to('cpu')


x = torch.ones(32, 2304, 256)

test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (73728x256 and 1x1)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(32, 2304, 256)), Parameter(FakeTensor(..., size=(1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(1,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [73728, 256] X [1, 1].

from user code:
   File "<string>", line 26, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''