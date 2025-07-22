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
        self.conv_transpose1 = torch.nn.ConvTranspose2d(1000, 32, 4, stride=1, padding=0, output_padding=0)
        self.conv_transpose2 = torch.nn.ConvTranspose2d(32, 32, 2, stride=1, padding=0, output_padding=0)
        self.conv_transpose3 = torch.nn.ConvTranspose2d(32, 3, 2, stride=2, padding=0, output_padding=0)

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
        v11 = v10 * 0.5
        v12 = v10 * v10 * v10
        v13 = v12 * 0.044715
        v14 = v10 + v13
        v15 = v14 * 0.7978845608028654
        v16 = torch.tanh(v15)
        v17 = v16 + 1
        v18 = v11 * v17
        v19 = self.conv_transpose3(v18)
        return v19



func = Model().to('cpu')


x1 = torch.randn(1, 32, 24, 24)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [1000, 32, 4, 4], expected input[1, 32, 24, 24] to have 1000 channels, but got 32 channels instead

jit:
Failed running call_function <built-in method conv_transpose2d of type object at 0x7f56a4596ec0>(*(FakeTensor(..., size=(1, s0, s1, s2)), Parameter(FakeTensor(..., size=(1000, 32, 4, 4), requires_grad=True)), Parameter(FakeTensor(..., size=(32,), requires_grad=True)), (1, 1), (0, 0), (0, 0), 1, (1, 1)), **{}):
Given transposed=1, weight of size [1000, 32, 4, 4], expected input[1, s0, s1, s2] to have 1000 channels, but got s0 channels instead

from user code:
   File "<string>", line 22, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 1162, in forward
    return F.conv_transpose2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''