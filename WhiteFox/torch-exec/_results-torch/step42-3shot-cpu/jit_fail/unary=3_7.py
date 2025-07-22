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
        self.conv1 = torch.nn.Conv2d(190, 190, (11, 33), stride=3, padding=0)
        self.conv2 = torch.nn.Conv2d(190, 139, 3, stride=3, padding=1)
        self.conv3 = torch.nn.ConvTranspose2d(202, 113, 12, stride=2, padding=0)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5
        v7 = self.conv2(v6)
        v8 = v7 * 0.5
        v9 = v7 * 0.7071067811865476
        v10 = torch.erf(v9)
        v11 = v10 + 1
        v12 = v8 * v11
        v13 = self.conv3(v12)
        return v13



func = Model().to('cpu')


x1 = torch.randn(1, 190, 240, 240)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [202, 113, 12, 12], expected input[1, 139, 26, 24] to have 202 channels, but got 139 channels instead

jit:
Failed running call_function <built-in method conv_transpose2d of type object at 0x74496ff96ec0>(*(FakeTensor(..., size=(1, 139, 26, 24)), Parameter(FakeTensor(..., size=(202, 113, 12, 12), requires_grad=True)), Parameter(FakeTensor(..., size=(113,), requires_grad=True)), (2, 2), (0, 0), (0, 0), 1, (1, 1)), **{}):
Given transposed=1, weight of size [202, 113, 12, 12], expected input[1, 139, 26, 24] to have 202 channels, but got 139 channels instead

from user code:
   File "<string>", line 34, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 1162, in forward
    return F.conv_transpose2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''