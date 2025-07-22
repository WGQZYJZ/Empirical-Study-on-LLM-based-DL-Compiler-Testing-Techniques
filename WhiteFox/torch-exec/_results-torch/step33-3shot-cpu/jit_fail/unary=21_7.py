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

class ModelTanh(torch.nn.Module):

    def __init__(self):
        super(ModelTanh, self).__init__()
        self.conv1 = torch.nn.Conv2d(25, 8, 3, padding=1, stride=2)
        self.conv2 = torch.nn.Conv2d(8, 17, 3, padding=1, stride=2)
        self.conv3 = torch.nn.Conv2d(17, 19, 3, padding=1, stride=2)
        self.conv4 = torch.nn.Conv2d(19, 32, 3, padding=1, stride=2)
        self.conv5 = torch.nn.Conv2d(32, 48, 7, padding=3, stride=1)
        self.relu = torch.nn.ReLU()
        self.pool = torch.nn.MaxPool2d(9)

    def forward(self, input_tensor):
        x1 = self.conv1(input_tensor)
        x2 = self.relu(x1)
        x3 = self.pool(x2)
        x4 = self.conv2(x3)
        x5 = self.relu(x4)
        x6 = self.pool(x5)
        x7 = self.conv3(x6)
        x8 = self.relu(x7)
        x9 = self.pool(x8)
        x10 = self.conv4(x9)
        x11 = self.relu(x10)
        x12 = self.pool(x11)
        x13 = self.conv5(x12)
        x14 = self.relu(x13)
        x15 = self.pool(x14)
        return x15



func = ModelTanh().to('cpu')


input_tensor = torch.randn(1, 25, 128, 128)

test_inputs = [input_tensor]

# JIT_FAIL
'''
direct:
Given input size: (17x4x4). Calculated output size: (17x0x0). Output size is too small

jit:
Failed running call_function <function boolean_dispatch.<locals>.fn at 0x78af77f61ee0>(*(FakeTensor(..., size=(1, 17, 4, 4)), 9, 9, 0, 1), **{'ceil_mode': False, 'return_indices': False}):
Given input size: (17x4x4). Calculated output size: (17x0x0). Output size is too small

from user code:
   File "<string>", line 31, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/pooling.py", line 213, in forward
    return F.max_pool2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''