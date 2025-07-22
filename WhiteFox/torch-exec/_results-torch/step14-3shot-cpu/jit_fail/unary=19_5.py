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
        self.linear = torch.nn.Linear(224, 224)

    def forward(self, x1):
        v1 = x1.view(-1, 224 * 224)
        v2 = self.linear(v1)
        v3 = torch.sigmoid(v2)
        return v3


func = Model().to('cpu')


x1 = torch.randn(1, 3, 224, 224)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (3x50176 and 224x224)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(s0, s1*s2)), Parameter(FakeTensor(..., size=(224, 224), requires_grad=True)), Parameter(FakeTensor(..., size=(224,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [s0, s1*s2] X [224, 224].

from user code:
   File "<string>", line 21, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''