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

    def __init__(self, min_value=5.8, max_value=2.1):
        super().__init__()
        self.sigmoid = torch.nn.Sigmoid()
        self.conv_transpose = torch.nn.ConvTranspose3d(1, 1, 1, stride=1)
        self.tanh_ = torch.nn.Tanh()
        self.relu_ = torch.nn.ReLU()
        self.softmax = torch.nn.Softmax()
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x):
        v1 = self.conv_transpose(x)
        v2 = torch.clamp_min(v1, self.min_value)
        v3 = torch.clamp_max(v2, self.max_value)
        v4 = self.tanh_(v3)
        v5 = self.relu_(v4)
        v6 = self.softmax(v5)
        return v6



func = Model().to('cpu')


x = torch.randn(3, 1, 4, 4)

test_inputs = [x]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [1, 1, 1, 1, 1], expected input[1, 3, 1, 4, 4] to have 1 channels, but got 3 channels instead

jit:
Failed running call_function <built-in method conv_transpose3d of type object at 0x7cb272d96ec0>(*(FakeTensor(..., size=(3, 1, 4, 4)), Parameter(FakeTensor(..., size=(1, 1, 1, 1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(1,), requires_grad=True)), (1, 1, 1), (0, 0, 0), (0, 0, 0), 1, (1, 1, 1)), **{}):
Given transposed=1, weight of size [1, 1, 1, 1, 1], expected input[1, 3, 1, 4, 4] to have 1 channels, but got 3 channels instead

from user code:
   File "<string>", line 26, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 1347, in forward
    return F.conv_transpose3d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''