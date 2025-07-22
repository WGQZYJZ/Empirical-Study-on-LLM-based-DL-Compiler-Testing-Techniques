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

class Model(nn.Module):

    def __init__(self):
        super().__init__()
        self.layers1 = nn.Linear(4, 4)
        self.layers2 = nn.Linear(4, 18)
        self.layers3 = nn.Linear(18, 2)
        self.layers4 = nn.Linear(2, 6)

    def forward(self, x):
        x = self.layers1(x)
        x = F.relu(x, inplace=False)
        x = torch.cat((x, x), dim=1)
        x = F.relu(x, inplace=False)
        x = torch.cat((x, x, x, x, x, x), dim=1)
        x = F.relu(x, inplace=False)
        x = self.layers2(x)
        x = F.relu(x, inplace=False)
        x = self.layers3(x)
        x = F.max_pool2d(x, kernel_size=2, stride=1)
        x = self.layers4(x)
        x = F.max_pool2d(x, kernel_size=2, stride=1)
        return x



func = Model().to('cpu')


x = torch.randn(2, 4)

test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (2x48 and 4x18)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(2, 48)), Parameter(FakeTensor(..., size=(18, 4), requires_grad=True)), Parameter(FakeTensor(..., size=(18,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [2, 48] X [4, 18].

from user code:
   File "<string>", line 29, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''