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
        self.conv1 = torch.nn.Conv2d(1, 6, 3, padding=3, bias=False, stride=3)
        self.conv12 = torch.nn.Conv2d(6, 24, 1, padding=0, stride=1, bias=False)
        self.conv2 = torch.nn.ConvTranspose2d(1, 4, 5, stride=5, padding=5, bias=False)
        self.conv22 = torch.nn.ConvTranspose2d(4, 4, 2, stride=2, padding=2, bias=False)
        self.conv3 = torch.nn.Conv2d(4, 8, 3, padding=2, stride=2, bias=False)
        self.relu = torch.nn.ReLU()
        self.prelu = torch.nn.PReLU(num_parameters=1, init=0.25)
        self.relu6 = torch.nn.ReLU6()

    def forward(self, x):
        v20 = 0.7978845608028654
        v19 = 0.044715
        v18 = 0.5
        v15 = self.conv12(x)
        v11 = self.conv2(v15)
        v6 = self.conv3(v11)
        v13 = self.conv22(v15)
        v22 = self.prelu(v6)
        v21 = self.conv1(x)
        v5 = self.conv22(v21)
        v16 = self.relu(v21)
        v9 = v22 * v13
        v12 = v16 + v19
        v7 = v22 * v12
        v8 = v16 + v20
        v10 = v18 * v22
        v14 = v10 * v9
        return v14



func = Model().to('cpu')


x = torch.randn(1, 1, 18, 18)

test_inputs = [x]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [24, 6, 1, 1], expected input[1, 1, 18, 18] to have 6 channels, but got 1 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x7d0047596ec0>(*(FakeTensor(..., size=(1, 1, 18, 18)), Parameter(FakeTensor(..., size=(24, 6, 1, 1), requires_grad=True)), None, (1, 1), (0, 0), (1, 1), 1), **{}):
Given groups=1, weight of size [24, 6, 1, 1], expected input[1, 1, 18, 18] to have 6 channels, but got 1 channels instead

from user code:
   File "<string>", line 30, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''