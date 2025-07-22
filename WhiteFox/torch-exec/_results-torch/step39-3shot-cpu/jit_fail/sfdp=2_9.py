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
        self.linear_q = torch.nn.Linear(16, 32)
        self.linear_k = torch.nn.Linear(20, 32)
        self.linear_v = torch.nn.Linear(4, 32)

    def forward(self, x1, x2):
        q = self.linear_q(x1).unsqueeze(1)
        v = self.linear_v(x2)
        k = self.linear_k(x2).transpose(-2, -1)
        scaled_q = q
        softmax_q = scaled_q.softmax(dim=-1)
        dropout_q = torch.nn.functional.dropout(softmax_q, p=0.5)
        output = dropout_q.matmul(v)
        return output


func = Model().to('cpu')


x1 = torch.randn(4, 16)

x2 = torch.randn(20, 4)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (20x4 and 20x32)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(20, 4)), Parameter(FakeTensor(..., size=(32, 20), requires_grad=True)), Parameter(FakeTensor(..., size=(32,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [20, 4] X [20, 32].

from user code:
   File "<string>", line 24, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''