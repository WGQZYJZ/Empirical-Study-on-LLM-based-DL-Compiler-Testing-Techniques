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

    def __init__(self, d_model=512, n_head=8, d_head=64, drop_ratio=0.1):
        super().__init__()
        self.scale_factor = torch.tensor(d_head ** (-0.5))
        self.dropout_p = drop_ratio
        self.Q = torch.nn.Linear(d_model, d_head * n_head)
        self.K = torch.nn.Linear(d_model, d_head * n_head)
        self.V = torch.nn.Linear(d_model, d_head * n_head)

    def forward(self, x1):
        q = self.Q(x1)
        k = self.K(x1)
        v = self.V(x1)
        qk = torch.matmul(q, k.transpose(-2, -1))
        scaled_qk = qk.mul(self.scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = dropout_qk.matmul(v)
        return output


func = Model().to('cpu')


x1 = torch.randn(1, 512, 128, 10)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (65536x10 and 512x512)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 512, 128, 10)), Parameter(FakeTensor(..., size=(512, 512), requires_grad=True)), Parameter(FakeTensor(..., size=(512,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [65536, 10] X [512, 512].

from user code:
   File "<string>", line 24, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''