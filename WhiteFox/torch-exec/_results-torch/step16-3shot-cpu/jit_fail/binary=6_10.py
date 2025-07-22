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

    def __init__(self, in_shape: int=512, out_shape: int=1152, num: int=512, bias: bool=False):
        super().__init__()
        self.dense1 = torch.nn.Linear(in_shape, out_shape, bias=bias)
        self.dense2 = torch.nn.Linear(out_shape, num, bias=bias)

    def forward(self, x):
        v1 = torch.flatten(x, start_dim=1)
        v2 = self.dense1(v1)
        v3 = v2 - 0.5
        v4 = self.dense2(v3)
        return v4


func = Model().to('cpu')


x1 = torch.randn(1, 3, 258, 258)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x199692 and 512x1152)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 199692)), Parameter(FakeTensor(..., size=(1152, 512), requires_grad=True)), None), **{}):
a and b must have same reduction dim, but got [1, 199692] X [512, 1152].

from user code:
   File "<string>", line 22, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''