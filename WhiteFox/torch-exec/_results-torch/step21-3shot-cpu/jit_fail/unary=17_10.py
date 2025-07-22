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
        self.conv = torch.nn.ConvTranspose2d(2, 4, (2, 3), stride=(2, 1), padding=(21, 17))
        self.conv1 = torch.nn.ConvTranspose2d(3, 2, 1, stride=1, padding=0)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.relu(v1)
        v3 = self.conv1(v2)
        return v3



func = Model().to('cpu')


x1 = torch.randn(1, 2, 224, 224)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [3, 2, 1, 1], expected input[1, 4, 406, 192] to have 3 channels, but got 4 channels instead

jit:
Failed running call_function <built-in method conv_transpose2d of type object at 0x7f3a51f96ec0>(*(FakeTensor(..., size=(1, 4, 2*s1 - 42, s2 - 32)), Parameter(FakeTensor(..., size=(3, 2, 1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(2,), requires_grad=True)), (1, 1), (0, 0), (0, 0), 1, (1, 1)), **{}):
Given transposed=1, weight of size [3, 2, 1, 1], expected input[1, 4, 2*s1 - 42, s2 - 32] to have 3 channels, but got 4 channels instead

from user code:
   File "<string>", line 23, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 1162, in forward
    return F.conv_transpose2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''