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
        self.trans_3 = torch.nn.ConvTranspose3d(4, 1, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.trans_3(x1)
        v2 = torch.sigmoid(v1)
        v3 = v1 * v2
        return v3



func = Model().to('cpu')


x1 = torch.randn(1, 1, 2, 2, 2)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [4, 1, 1, 1, 1], expected input[1, 1, 2, 2, 2] to have 4 channels, but got 1 channels instead

jit:
Failed running call_function <built-in method conv_transpose3d of type object at 0x7ca199d96ec0>(*(FakeTensor(..., size=(1, 1, s0, s1, s2)), Parameter(FakeTensor(..., size=(4, 1, 1, 1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(1,), requires_grad=True)), (1, 1, 1), (1, 1, 1), (0, 0, 0), 1, (1, 1, 1)), **{}):
Given transposed=1, weight of size [4, 1, 1, 1, 1], expected input[1, 1, s0, s1, s2] to have 4 channels, but got 1 channels instead

from user code:
   File "<string>", line 20, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 1347, in forward
    return F.conv_transpose3d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''