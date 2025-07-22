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
        self.linear1 = torch.nn.Linear(6, 5)
        self.linear2 = torch.nn.Linear(7, 8)

    def forward(self, x):
        if x.shape[1] == 8:
            x = x.transpose(1, 2)
        z = self.linear2(x)
        z = z.reshape(8, 4, 3, 2)
        y = self.linear1(z)
        return y



func = Model().to('cuda')


x = torch.randn(1, 1, 8, 6)

test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (8x6 and 7x8)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., device='cuda:0', size=(1, 1, s0, s1)), Parameter(FakeTensor(..., device='cuda:0', size=(8, 7), requires_grad=True)), Parameter(FakeTensor(..., device='cuda:0', size=(8,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [s0, s1] X [7, 8].

from user code:
   File "<string>", line 23, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''