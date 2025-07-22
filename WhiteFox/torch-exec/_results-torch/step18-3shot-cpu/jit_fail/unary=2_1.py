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
        self.conv1 = torch.nn.Conv2d(6, 12, 2, stride=4, padding=1)
        self.conv2 = torch.nn.Conv2d(12, 32, 3, stride=2, padding=1, dilation=2)
        self.layer_norm1 = torch.nn.LayerNorm((32,))
        self.conv3 = torch.nn.Conv2d(32, 64, 1)
        self.layer_norm2 = torch.nn.LayerNorm((64,), elementwise_affine=False)
        self.layer_norm3 = torch.nn.LayerNorm((64,))
        self.conv_transpose1 = torch.nn.ConvTranspose2d(64, 64, 1, stride=1, padding=1)
        self.layer_norm4 = torch.nn.LayerNorm((64,))

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        v3 = self.layer_norm1(v2)
        v4 = self.conv3(v3)
        v5 = self.layer_norm2(v4)
        v6 = v5 * 0.5
        v7 = v5 * v5 * v5
        v8 = v7 * 0.044715
        v9 = v5 + v8
        v10 = v9 * 0.7978845608028654
        v11 = torch.tanh(v10)
        v12 = v10 + 1
        v13 = v6 * v11
        v14 = v12 * v3
        v15 = self.layer_norm3(v14)
        v16 = self.conv_transpose1(v15)
        v17 = self.layer_norm4(v16)
        v18 = v17 * v12
        return v13



func = Model().to('cpu')


x1 = torch.randn(2, 6, 7, 9)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (4 x 5). Kernel size: (5 x 5). Kernel size can't be greater than actual input size

jit:
Failed running call_function <built-in method conv2d of type object at 0x7b7befd96ec0>(*(FakeTensor(..., size=(2, 12, 2, 3)), Parameter(FakeTensor(..., size=(32, 12, 3, 3), requires_grad=True)), Parameter(FakeTensor(..., size=(32,), requires_grad=True)), (2, 2), (1, 1), (2, 2), 1), **{}):
Calculated padded input size per channel: (4 x 5). Kernel size: (5 x 5). Kernel size can't be greater than actual input size

from user code:
   File "<string>", line 28, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''