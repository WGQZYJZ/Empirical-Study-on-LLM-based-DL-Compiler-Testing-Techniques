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
        self.conv_transpose1 = torch.nn.ConvTranspose2d(512, 576, kernel_size=(7, 1), stride=(1, 1), padding=(521, 0), dilation=1, groups=1, bias=False)

    def forward(self, x1):
        v1 = self.conv_transpose1(x1)
        v2 = torch.tanh(v1)
        return v2



func = Model().to('cpu')


x1 = torch.randn(1, 512, 1, 1)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given input size per channel: (1 x 1). Calculated output size per channel: (-1035 x 1). Output size is too small

jit:
Failed running call_function <built-in method conv_transpose2d of type object at 0x7f63b5f96ec0>(*(FakeTensor(..., size=(1, 512, 1, 1)), Parameter(FakeTensor(..., size=(512, 576, 7, 1), requires_grad=True)), None, (1, 1), (521, 0), (0, 0), 1, (1, 1)), **{}):
Trying to create tensor with negative dimension -1035: [1, 576, -1035, 1]

from user code:
   File "<string>", line 20, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 1162, in forward
    return F.conv_transpose2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''