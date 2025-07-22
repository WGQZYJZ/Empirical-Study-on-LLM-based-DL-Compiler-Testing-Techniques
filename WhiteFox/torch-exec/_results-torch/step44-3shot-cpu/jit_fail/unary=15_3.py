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
        self.conv = torch.nn.Conv2d(3, 1, 3, stride=1, padding=3, dilation=2)
        self.layer1 = torch.nn.modules.pooling.MaxPool2d(3, stride=2, padding=1)
        self.layer2 = torch.nn.ReLU6(True)

    def forward(self, x1):
        v1 = self.conv(x1)
        for layer in self.children():
            v1 = layer(v1)
        return v1



func = Model().to('cpu')


x1 = torch.randn(1, 3, 224, 224)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [1, 3, 3, 3], expected input[1, 1, 226, 226] to have 3 channels, but got 1 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x79de4fd96ec0>(*(FakeTensor(..., size=(1, 1, 226, 226)), Parameter(FakeTensor(..., size=(1, 3, 3, 3), requires_grad=True)), Parameter(FakeTensor(..., size=(1,), requires_grad=True)), (1, 1), (3, 3), (2, 2), 1), **{}):
Given groups=1, weight of size [1, 3, 3, 3], expected input[1, 1, 226, 226] to have 3 channels, but got 1 channels instead

from user code:
   File "<string>", line 24, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''