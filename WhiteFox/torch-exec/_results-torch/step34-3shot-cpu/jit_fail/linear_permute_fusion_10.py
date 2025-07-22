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
        self.linear = torch.nn.Linear(2, 2)
        self.conv = torch.nn.Conv2d(1, 1, 2, 2, 1)

    def forward(self, x1):
        t1 = self.conv(x1)
        t3 = t1.permute(0, 2, 3, 1)
        return self.linear(t3)



func = Model().to('cpu')


x1 = torch.randn(3, 1, 2, 2)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (12x1 and 2x2)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(s0, ((s1//2)) + 1, ((s2//2)) + 1, 1)), Parameter(FakeTensor(..., size=(2, 2), requires_grad=True)), Parameter(FakeTensor(..., size=(2,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [s0*(((s1//2)) + 1)*(((s2//2)) + 1), 1] X [2, 2].

from user code:
   File "<string>", line 23, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''