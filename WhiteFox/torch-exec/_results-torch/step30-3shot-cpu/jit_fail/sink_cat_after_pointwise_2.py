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
        self.t = torch.nn.Linear(3, 5)

    def forward(self, x):
        t1 = torch.cat((x, x), dim=1)
        t2 = t1.view(x.shape[0], -1).tanh()
        t3 = t2.view(x.shape[0], -1)
        t4 = torch.relu(t3)
        t5 = t4.view(x.shape[0], -1).sigmoid()
        t6 = self.t(t5)
        x = t6
        return x



func = Model().to('cpu')


x = torch.randn(2, 3, 4)

test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (2x24 and 3x5)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(2, 24)), Parameter(FakeTensor(..., size=(5, 3), requires_grad=True)), Parameter(FakeTensor(..., size=(5,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [2, 24] X [3, 5].

from user code:
   File "<string>", line 25, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''