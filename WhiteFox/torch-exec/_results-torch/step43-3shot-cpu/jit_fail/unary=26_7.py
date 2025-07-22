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
        self.conv_t = torch.nn.ConvTranspose2d(4, 8, 5, stride=1, padding=5, bias=False)

    def forward(self, x1):
        y1 = self.conv_t(x1)
        y2 = y1 > 0
        y3 = y1 * 5.893
        y4 = torch.where(y2, y1, y3)
        return y4



func = Model().to('cpu')


x1 = torch.randn(1, 4, 1, 7, requires_grad=False)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
could not construct a memory descriptor using a format tag

jit:
Failed running call_function <built-in method conv_transpose2d of type object at 0x78dff3396ec0>(*(FakeTensor(..., size=(1, 4, 1, 7)), Parameter(FakeTensor(..., size=(4, 8, 5, 5), requires_grad=True)), None, (1, 1), (5, 5), (0, 0), 1, (1, 1)), **{}):
Trying to create tensor with negative dimension -5: [1, 8, -5, 1]

from user code:
   File "<string>", line 20, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 1162, in forward
    return F.conv_transpose2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''