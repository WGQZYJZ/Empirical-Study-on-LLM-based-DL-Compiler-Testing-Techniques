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
        self.conv_t = torch.nn.ConvTranspose2d(1, 3, 1, stride=2, padding=21, bias=True)

    def forward(self, x5):
        z1 = self.conv_t(x5)
        z2 = z1 > 0
        z3 = z1 * -0.752
        z4 = torch.where(z2, z1, z3)
        return torch.nn.functional.interpolate(z4, scale_factor=[1.0, 1.0])



func = Model().to('cpu')


x5 = torch.randn(3, 1, 7, 31)

test_inputs = [x5]

# JIT_FAIL
'''
direct:
could not construct a memory descriptor using a format tag

jit:
Failed running call_function <built-in method conv_transpose2d of type object at 0x7839b8196ec0>(*(FakeTensor(..., size=(3, 1, 7, 31)), Parameter(FakeTensor(..., size=(1, 3, 1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(3,), requires_grad=True)), (2, 2), (21, 21), (0, 0), 1, (1, 1)), **{}):
Trying to create tensor with negative dimension -29: [3, 3, -29, 19]

from user code:
   File "<string>", line 20, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 1162, in forward
    return F.conv_transpose2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''