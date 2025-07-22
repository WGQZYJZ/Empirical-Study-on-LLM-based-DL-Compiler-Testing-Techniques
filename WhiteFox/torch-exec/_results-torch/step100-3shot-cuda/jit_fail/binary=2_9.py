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
        self.conv1 = torch.nn.Conv2d(3, 8, kernel_size=(3, 3), stride=(3, 3), padding=(1, 1))
        self.conv2 = torch.nn.Conv2d(3, 8, kernel_size=(2, 2), stride=(1, 1), padding=(1, 1))
        self.conv3 = torch.nn.Conv2d(8, 8, kernel_size=(2, 2), stride=(2, 2), padding=(1, 1))
        self.conv4 = torch.nn.Conv2d(8, 8, kernel_size=(3, 2), stride=(1, 1), padding=(1, 1))
        self.conv5 = torch.nn.Conv2d(8, 8, kernel_size=(1, 1), stride=(2, 2), padding=(1, 1))

    def forward(self, x):
        l1 = {self.conv1}
        l2 = {x, self.conv2}
        l3 = {x, self.conv3}
        v1 = self.conv1(x)
        v2 = self.conv2(l1.pop() + self.conv4(l2.pop() + l3.pop()))
        v3 = v2 - v1
        v4 = self.conv5(v3)
        return v4



func = Model().to('cuda')


x = torch.randn(1, 3, 32, 32)

test_inputs = [x]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [8, 8, 3, 2], expected input[1, 3, 32, 32] to have 8 channels, but got 3 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x795254b96ec0>(*(FakeTensor(..., device='cuda:0', size=(1, 3, 32, 32)), Parameter(FakeTensor(..., device='cuda:0', size=(8, 8, 3, 2), requires_grad=True)), Parameter(FakeTensor(..., device='cuda:0', size=(8,), requires_grad=True)), (1, 1), (1, 1), (1, 1), 1), **{}):
Given groups=1, weight of size [8, 8, 3, 2], expected input[1, 3, 32, 32] to have 8 channels, but got 3 channels instead

from user code:
   File "<string>", line 28, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''