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
        self.fc = torch.nn.Linear(16, 4)

    def forward(self, x1, x2):
        q = torch.cat([x1, x2], dim=-1)
        k = self.fc(q)
        inv_scale_factor = 1
        dropout_p = 0
        v = torch.cat([x1, x2], dim=-1)
        qk = torch.matmul(q, k.transpose(-2, -1))
        scaled_qk = qk / inv_scale_factor
        softmax_qk = torch.softmax(scaled_qk, dim=-1)
        dropout_qk = F.dropout(softmax_qk, p=dropout_p)
        output = torch.matmul(dropout_qk, v)
        return output


func = Model().to('cpu')


x1 = torch.randn(1, 16)

x2 = torch.randn(1, 16)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x32 and 16x4)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 32)), Parameter(FakeTensor(..., size=(4, 16), requires_grad=True)), Parameter(FakeTensor(..., size=(4,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [1, 32] X [16, 4].

from user code:
   File "<string>", line 21, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''