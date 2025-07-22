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

class LeakyReLUModel(torch.nn.Module):

    def __init__(self, channel_size, nonnegative=True, input_scale=0.001):
        super().__init__()
        self.channel_size = channel_size
        self.nonnegative = nonnegative
        self.input_scale = input_scale
        self.conv1 = torch.nn.Conv2d(channel_size, channel_size, 3, stride=1, padding=1)
        self.bn1 = torch.nn.BatchNorm2d(channel_size)

    def forward(self, x):
        input_prescale = x * self.input_scale
        conv1 = self.conv1(input_prescale)
        bn = self.bn1(conv1)
        relu = (self.nonnegative & (bn >= 0)) * (bn - 0.01 * bn * (bn < 0)) + self.nonnegative * bn
        relu *= 1.0 / self.input_scale
        return relu

class Model(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(128, 512, 1, stride=1, padding=0)
        self.conv2 = torch.nn.Conv2d(512, 512, 1, stride=1, padding=0)
        self.fc = torch.nn.Linear(512, 512)

    def forward(self, x):
        feature1 = self.conv1(x).mean((-2, -1))
        feature2 = self.conv2(feature1)
        feature3 = feature2.mean((-2, -1))
        out = self.fc(feature3)
        return out



func = Model().to('cpu')

input_size = 224
input_size = 224

x = torch.randn((1, 128, input_size, input_size), requires_grad=True)

test_inputs = [x]

# JIT_FAIL
'''
direct:
Expected 3D (unbatched) or 4D (batched) input to conv2d, but got input of size: [1, 512]

jit:
Failed running call_function <built-in method conv2d of type object at 0x7f2b88196ec0>(*(FakeTensor(..., size=(1, 512)), Parameter(FakeTensor(..., size=(512, 512, 1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(512,), requires_grad=True)), (1, 1), (0, 0), (1, 1), 1), **{}):
Expected 3D (unbatched) or 4D (batched) input to conv2d, but got input of size: [1, 512]

from user code:
   File "<string>", line 41, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''