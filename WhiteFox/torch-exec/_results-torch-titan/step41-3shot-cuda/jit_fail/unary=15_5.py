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
        self.conv1 = torch.nn.Conv2d(3, 16, 3, stride=1, padding=1)
        self.pool1 = torch.nn.MaxPool2d(2)
        self.conv2 = torch.nn.Conv2d(16, 32, 5, stride=1, padding=1)
        self.pool2 = torch.nn.AvgPool2d(2)
        self.conv3 = torch.nn.Conv2d(32, 64, 7, stride=1, padding=1)

    def forward(self, x1):
        v1 = torch.nn.functional.interpolate(self.pool1(self.conv1(x1)), None, 5, 'linear')
        v2 = torch.nn.functional.interpolate(self.pool2(self.conv2(v1)), None, 2, 'nearest')
        v3 = self.conv3(v2)
        return v3




func = Model().to('cuda')



x1 = torch.randn(1, 3, 320, 256)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Got 4D input, but linear mode needs 3D input

jit:
Failed running call_function <function interpolate at 0x7664c61b8430>(*(FakeTensor(..., device='cuda:0', size=(1, 16, 160, 128)), None, 5, 'linear'), **{}):
Got 4D input, but linear mode needs 3D input

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''