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

    def __init__(self, dim):
        super().__init__()
        self.qk = torch.nn.Linear(dim, dim)
        self.value = torch.nn.Linear(dim, dim)

    def forward(self, x1, x2, x3, input_mask):
        qk = self.qk(x1)
        value = self.value(x2)
        inv_scale_factor = torch.rsqrt(torch.sum(qk.mul(qk), dim=-1, keepdim=True))
        qk = qk.mul(inv_scale_factor).softmax(dim=-1)
        input_mask = input_mask.to(torch.float)
        dropout_qk = torch.nn.functional.dropout(qk, p=0.5)
        qk = qk.mul(input_mask)
        output = qk.matmul(value)
        output = output.unsqueeze(0)
        return output


dim = 1
func = Model(8).to('cpu')


x1 = torch.randn(1, 8, 10, 16)

x2 = torch.randn(1, 8, 16, 10)

x3 = torch.randn(1, 10, 16)

input_mask = torch.randn(1, 8, 10, 16)

test_inputs = [x1, x2, x3, input_mask]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (80x16 and 8x8)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 8, 10, 16)), Parameter(FakeTensor(..., size=(8, 8), requires_grad=True)), Parameter(FakeTensor(..., size=(8,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [80, 16] X [8, 8].

from user code:
   File "<string>", line 21, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''