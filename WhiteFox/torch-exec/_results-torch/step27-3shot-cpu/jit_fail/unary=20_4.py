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
        self.conv1 = torch.nn.Conv2d(1, 20, 5, 1)
        self.conv2 = torch.nn.ConvTranspose2d(5, 6, kernel_size=(5, 5))

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        v3 = torch.sigmoid(v2)
        return v3



func = Model().to('cpu')


x1 = torch.randn(10, 1, 28, 28)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [5, 6, 5, 5], expected input[10, 20, 24, 24] to have 5 channels, but got 20 channels instead

jit:
Failed running call_function <built-in method conv_transpose2d of type object at 0x7fa56e596ec0>(*(FakeTensor(..., size=(s0, 20, s1 - 4, s2 - 4)), Parameter(FakeTensor(..., size=(5, 6, 5, 5), requires_grad=True)), Parameter(FakeTensor(..., size=(6,), requires_grad=True)), (1, 1), (0, 0), (0, 0), 1, (1, 1)), **{}):
Given transposed=1, weight of size [5, 6, 5, 5], expected input[s0, 20, s1 - 4, s2 - 4] to have 5 channels, but got 20 channels instead

from user code:
   File "<string>", line 22, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 1162, in forward
    return F.conv_transpose2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''