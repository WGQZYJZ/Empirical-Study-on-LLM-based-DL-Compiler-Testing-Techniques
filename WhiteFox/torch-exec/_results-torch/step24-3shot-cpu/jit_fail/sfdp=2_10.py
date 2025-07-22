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

    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)

    def forward(self, x, y):
        z = torch.cat((x, y), dim=-1)
        q = self.linear(z)
        k = self.linear(z)
        v = self.linear(z)
        qk = torch.matmul(q, k.transpose(-2, -1))
        scaled_qk = qk.div(8)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.39999995)
        output = dropout_qk.matmul(v)
        return output


func = Model().to('cpu')


x = torch.randn(2, 3)

y = torch.randn(2, 3)

test_inputs = [x, y]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (2x6 and 3x8)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(2, 6)), Parameter(FakeTensor(..., size=(8, 3), requires_grad=True)), Parameter(FakeTensor(..., size=(8,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [2, 6] X [3, 8].

from user code:
   File "<string>", line 21, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''