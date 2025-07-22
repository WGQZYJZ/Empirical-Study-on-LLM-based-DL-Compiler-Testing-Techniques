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
        self.conv2d = torch.nn.Conv2d(16, 16, 3, stride=1, padding=2)
        self.conv_transpose = torch.nn.ConvTranspose2d(16, 4, 3, stride=-1, padding=0)

    def forward(self, x1):
        v1 = self.conv2d(x1)
        v2 = self.conv_transpose(v1)
        v3 = v2 + 3
        v4 = torch.clamp_min(v3, 0)
        v5 = torch.clamp_max(v4, 6)
        v6 = v5 / 6
        return v6



func = Model().to('cpu')


x1 = torch.randn(1, 16, 128, 128)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
non-positive stride is not supported

jit:
Failed running call_function <built-in method conv_transpose2d of type object at 0x7f1778196ec0>(*(FakeTensor(..., size=(1, 16, 130, 130)), Parameter(FakeTensor(..., size=(16, 4, 3, 3), requires_grad=True)), Parameter(FakeTensor(..., size=(4,), requires_grad=True)), (-1, -1), (0, 0), (0, 0), 1, (1, 1)), **{}):
non-positive stride is not supported

from user code:
   File "<string>", line 22, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 1162, in forward
    return F.conv_transpose2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''