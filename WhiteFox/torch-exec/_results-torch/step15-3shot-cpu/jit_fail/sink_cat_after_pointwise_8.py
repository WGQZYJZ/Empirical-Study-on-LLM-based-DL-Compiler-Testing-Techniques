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
        self.fc = torch.nn.Linear(20, 20)

    def forward(self, x):
        x = torch.cat((x, x), dim=1)
        x = self.fc(x)
        return x



func = Model().to('cpu')


x = torch.randn(5, 20)

test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (5x40 and 20x20)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(5, 40)), Parameter(FakeTensor(..., size=(20, 20), requires_grad=True)), Parameter(FakeTensor(..., size=(20,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [5, 40] X [20, 20].

from user code:
   File "<string>", line 21, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''