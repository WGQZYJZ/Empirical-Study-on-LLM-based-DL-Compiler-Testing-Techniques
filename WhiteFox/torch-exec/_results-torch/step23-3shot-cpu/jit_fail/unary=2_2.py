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
        self.conv1 = torch.nn.Conv2d(10, 12, 3, 1, 0)
        self.conv_transpose = torch.nn.ConvTranspose2d(12, 18, 2, 1, 4)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv_transpose(v1)
        v3 = v2 * 0.5
        v4 = v2 * v2 * v2
        v5 = v4 * 0.044715
        v6 = v2 + v5
        v7 = v6 * 0.7978845608028654
        v8 = torch.tanh(v7)
        v9 = v8 + 1
        v10 = v3 * v9
        return v10



func = Model().to('cpu')


x1 = torch.randn(3, 10, 6, 5)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
could not construct a memory descriptor using a format tag

jit:
Failed running call_function <built-in method conv_transpose2d of type object at 0x774a18396ec0>(*(FakeTensor(..., size=(3, 12, s1 - 2, s2 - 2)), Parameter(FakeTensor(..., size=(12, 18, 2, 2), requires_grad=True)), Parameter(FakeTensor(..., size=(18,), requires_grad=True)), (1, 1), (4, 4), (0, 0), 1, (1, 1)), **{}):
Trying to create tensor with negative dimension s1 - 9: [3, 18, s1 - 9, s2 - 9]

from user code:
   File "<string>", line 22, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 1162, in forward
    return F.conv_transpose2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''