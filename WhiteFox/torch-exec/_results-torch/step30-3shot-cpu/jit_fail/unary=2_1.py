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
        self.conv_transpose1 = torch.nn.ConvTranspose2d(3, 5, 3, padding=2)
        self.conv_transpose2 = torch.nn.ConvTranspose2d(5, 1, 2, padding=(8, 16))

    def forward(self, x1):
        v1 = self.conv_transpose1(x1)
        v2 = v1 * 0.5
        v3 = v1 * v1 * v1
        v4 = v3 * 0.044715
        v5 = v1 + v4
        v6 = v5 * 0.7978845608028654
        v7 = torch.tanh(v6)
        v8 = v7 + 1
        v9 = v2 * v8
        v10 = self.conv_transpose2(v9)
        v11 = v10 * 0.1
        v12 = v9 * 0.01
        v13 = v10 + v11
        v14 = v11 + v12
        v15 = v13 * v14
        return v15



func = Model().to('cpu')


x1 = torch.randn(1, 3, 122, 4)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given input size per channel: (120 x 2). Calculated output size per channel: (105 x -29). Output size is too small

jit:
Failed running call_function <built-in method conv_transpose2d of type object at 0x70a776396ec0>(*(FakeTensor(..., size=(1, 5, 120, 2)), Parameter(FakeTensor(..., size=(5, 1, 2, 2), requires_grad=True)), Parameter(FakeTensor(..., size=(1,), requires_grad=True)), (1, 1), (8, 16), (0, 0), 1, (1, 1)), **{}):
Trying to create tensor with negative dimension -29: [1, 1, 105, -29]

from user code:
   File "<string>", line 30, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 1162, in forward
    return F.conv_transpose2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''