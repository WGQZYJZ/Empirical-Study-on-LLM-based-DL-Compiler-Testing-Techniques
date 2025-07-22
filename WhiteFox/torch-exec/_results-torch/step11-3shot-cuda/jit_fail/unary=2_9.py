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
        self.deconv1 = torch.nn.ConvTranspose3d(3, 8, 1, stride=1, padding=1)
        self.deconv2 = torch.nn.ConvTranspose2d(8, 14, 1, stride=1, padding=1)
        self.deconv3 = torch.nn.ConvTranspose2d(14, 8, 5, stride=(1, 2), padding=(1, 2))
        self.deconv4 = torch.nn.Conv2d(8, 3, 3, stride=(1, 2), padding=(1, 2))
        self.deconv5 = torch.nn.ConvTranspose1d(16, 16, 32, stride=2, padding=15)

    def forward(self, x1):
        v1 = self.deconv1(x1)
        v2 = self.deconv2(v1)
        v3 = self.deconv3(v2)
        v4 = self.deconv4(v3)
        v5 = self.deconv5(v4)
        return v5



func = Model().to('cuda')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [3, 8, 1, 1, 1], expected input[1, 1, 3, 64, 64] to have 3 channels, but got 1 channels instead

jit:
Failed running call_function <built-in method conv_transpose3d of type object at 0x7e7cb5b96ec0>(*(FakeTensor(..., device='cuda:0', size=(1, 3, 64, 64)), Parameter(FakeTensor(..., device='cuda:0', size=(3, 8, 1, 1, 1), requires_grad=True)), Parameter(FakeTensor(..., device='cuda:0', size=(8,), requires_grad=True)), (1, 1, 1), (1, 1, 1), (0, 0, 0), 1, (1, 1, 1)), **{}):
Given transposed=1, weight of size [3, 8, 1, 1, 1], expected input[1, 1, 3, 64, 64] to have 3 channels, but got 1 channels instead

from user code:
   File "<string>", line 24, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 1347, in forward
    return F.conv_transpose3d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''