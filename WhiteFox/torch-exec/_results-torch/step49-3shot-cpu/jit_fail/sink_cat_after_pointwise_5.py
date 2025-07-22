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
        self.linear = torch.nn.Linear(5, 10).float()

    def forward(self, x):
        y = torch.cat((x, x), dim=1)
        x = y.view(-1)
        if x.shape[0] != 100:
            x = self.linear(x.unsqueeze(0))
        else:
            x = self.linear(x)
        return x



func = Model().to('cpu')


x = torch.randn(100, 5)

test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x1000 and 5x10)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 1000)), Parameter(FakeTensor(..., size=(10, 5), requires_grad=True)), Parameter(FakeTensor(..., size=(10,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [1, 1000] X [5, 10].

from user code:
   File "<string>", line 23, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''