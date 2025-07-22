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
        self.conv1 = torch.nn.Conv2d(3, 5, 15, stride=2, padding=0)
        self.conv2 = torch.nn.Conv2d(5, 10, 11, stride=1, padding=5)
        self.conv3 = torch.nn.Conv2d(5, 10, 11, stride=1, padding=5)
        self.conv4 = torch.nn.Conv2d(10, 20, 7, stride=1, padding=0)
        self.conv5 = torch.nn.Conv2d(20, 50, 7, stride=1, padding=0)
        self.conv6 = torch.nn.Conv2d(50, 100, 7, stride=1, padding=0)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v1 = torch.relu(v1)
        v1 = v1.type(torch.float16)
        v2 = self.conv2(v1)
        v2 = torch.relu(v2)
        v2 = v2.type(torch.float16)
        v3 = self.conv3(v2)
        v3 = torch.relu(v3)
        v3 = v3.type(torch.float16)
        v4 = self.conv4(v3)
        v4 = torch.relu(v4)
        v4 = v4.type(torch.float16)
        v5 = self.conv5(v4)
        v5 = torch.relu(v5)
        v5 = v5.type(torch.float16)
        v6 = self.conv6(v5)
        v6 = torch.relu(v6)
        v6 = v6.type(torch.float16)
        v6 = v6 * 12
        return v6 + 50



func = Model().to('cpu')


x1 = torch.randn(1, 3, 224, 224)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Input type (c10::Half) and bias type (float) should be the same

jit:
Failed running call_function <built-in method conv2d of type object at 0x7a3a7c196ec0>(*(FakeTensor(..., size=(1, 5, 105, 105), dtype=torch.float16), Parameter(FakeTensor(..., size=(10, 5, 11, 11), requires_grad=True)), Parameter(FakeTensor(..., size=(10,), requires_grad=True)), (1, 1), (5, 5), (1, 1), 1), **{}):
Input type (c10::Half) and bias type (float) should be the same

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