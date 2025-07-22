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
        self.linear1 = torch.nn.Linear(60, 40)
        self.linear2 = torch.nn.Linear(40, 20)
        self.linear3 = torch.nn.Linear(20, 1)

    def forward(self, inputs, weight1, weight2, weight3):
        v1 = self.linear1(inputs)
        v2 = self.linear2(inputs)
        v3 = self.linear3(inputs)
        return v1 + v2 + v3



func = Model().to('cpu')


inputs = torch.randn(1, 60)

weight1 = torch.randn(20, 60)

weight2 = torch.randn(20, 40)

weight3 = torch.randn(20, 20)

test_inputs = [inputs, weight1, weight2, weight3]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x60 and 40x20)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 60)), Parameter(FakeTensor(..., size=(20, 40), requires_grad=True)), Parameter(FakeTensor(..., size=(20,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [1, 60] X [40, 20].

from user code:
   File "<string>", line 23, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''