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
        self.deconv = torch.nn.ConvTranspose2d(8, 8, kernel_size=9, stride=9, padding=9)

    def forward(self, x):
        out = self.deconv(x)
        out = torch.sigmoid(out)
        return out



func = Model().to('cpu')


x = torch.randn(1, 8, 1, 1)

test_inputs = [x]

# JIT_FAIL
'''
direct:
could not construct a memory descriptor using a format tag

jit:
Failed running call_function <built-in method conv_transpose2d of type object at 0x71c40cd96ec0>(*(FakeTensor(..., size=(1, 8, 1, 1)), Parameter(FakeTensor(..., size=(8, 8, 9, 9), requires_grad=True)), Parameter(FakeTensor(..., size=(8,), requires_grad=True)), (9, 9), (9, 9), (0, 0), 1, (1, 1)), **{}):
Trying to create tensor with negative dimension -9: [1, 8, -9, -9]

from user code:
   File "<string>", line 20, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 1162, in forward
    return F.conv_transpose2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''