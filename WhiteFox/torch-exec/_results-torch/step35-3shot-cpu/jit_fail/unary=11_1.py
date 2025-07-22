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
        self.conv_transpose = torch.nn.ConvTranspose1d(50, 100, kernel_size=(21,), stride=(1,), dilation=(2,), groups=1, bias=False, padding=(49,))

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = v1 + 3
        v3 = torch.clamp_min(v2, 0)
        v4 = torch.clamp_max(v3, 6)
        v5 = v4 / 6
        return v5



func = Model().to('cpu')


x1 = torch.randn(100, 50, 1)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
could not construct a memory descriptor using a format tag

jit:
Failed running call_function <built-in method conv_transpose1d of type object at 0x770c6eb96ec0>(*(FakeTensor(..., size=(100, 50, 1)), Parameter(FakeTensor(..., size=(50, 100, 21), requires_grad=True)), None, (1,), (49,), (0,), 1, (2,)), **{}):
Trying to create tensor with negative dimension -57: [100, 100, -57]

from user code:
   File "<string>", line 20, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 974, in forward
    return F.conv_transpose1d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''