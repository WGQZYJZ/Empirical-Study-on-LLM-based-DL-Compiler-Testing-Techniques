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
        self.linear = torch.nn.Linear(3, 6, bias=False)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.zeros((x1.shape[0], 6, x1.shape[2], x1.shape[3]), dtype=torch.float32, device=x1.device)
        v3 = v1 - v2
        return v3


func = Model().to('cpu')


x1 = torch.randn(2, 3, 24, 32)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (144x32 and 3x6)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(s0, s1, s2, s3)), Parameter(FakeTensor(..., size=(6, 3), requires_grad=True)), None), **{}):
a and b must have same reduction dim, but got [s0*s1*s2, s3] X [3, 6].

from user code:
   File "<string>", line 20, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''