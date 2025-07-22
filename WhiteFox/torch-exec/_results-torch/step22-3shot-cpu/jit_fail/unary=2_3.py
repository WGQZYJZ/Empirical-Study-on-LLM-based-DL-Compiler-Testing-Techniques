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
        self.flatten = torch.nn.Flatten(start_dim=4, end_dim=4)

    def forward(self, x1):
        v1 = self.flatten(x1)
        v2 = v1 * 0.5
        v3 = v1 * v1 * v1
        v4 = v3 * 0.044715
        v5 = v1 + v4
        v6 = v5 * 0.7978845608028654
        v7 = torch.tanh(v6)
        v8 = v7 + 1
        v9 = v2 * v8
        return v9



func = Model().to('cpu')


x1 = torch.randn(4, 4, 4, 4)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Dimension out of range (expected to be in range of [-4, 3], but got 4)

jit:
Failed running call_method flatten(*(FakeTensor(..., size=(s0, s1, s2, s3)), 4, 4), **{}):
Dimension out of range (expected to be in range of [-4, 3], but got 4)

from user code:
   File "<string>", line 20, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/flatten.py", line 53, in forward
    return input.flatten(self.start_dim, self.end_dim)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''