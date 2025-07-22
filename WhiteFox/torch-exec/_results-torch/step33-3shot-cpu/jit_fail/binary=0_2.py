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
        self.conv = torch.nn.Conv2d(1, 1, (3, 3), stride=1, padding=1, groups=1)

    def forward(self, x1, x2, x3):
        x = self.conv(x1)
        x1 = x + x2
        x1 = self.conv(x1)
        x = self.conv(torch.cat((x1, x2), dim=1))
        x1 = torch.cat((x1, x3), dim=1)
        x2 = x1 + x
        x = self.conv(torch.cat((x1, x2)))
        x1 = x + self.conv(torch.cat((x1, x2)))
        x1 = x + self.conv(x)
        x2 = self.conv(x) + self.conv(x)
        x2 = x2 + x1
        x = self.conv(x1 + x2) + torch.cat((x1, x2))
        x = self.conv(x1 + self.conv(x2)) + torch.cat((x1, x2))
        x1 = torch.cat((x1, x2)) + self.conv(x)
        x1 = x + torch.cat((x1, x2))
        x1 = x + torch.cat((x1, x2), dim=1)
        x1 = torch.cat((x1, x2), dim=1) + torch.cat((x1, x2), dim=1)
        x = x1 + torch.cat((x1, x2), dim=1)
        x = x + x1
        x = torch.cat([torch.cat((x1, x2), dim=1), torch.cat((x1, x2), dim=1)])
        x1 = torch.cat((x, x1), dim=1) + x
        x = x1 + x
        x1 = x + x
        x2 = torch.cat((x, x1, x), dim=1)
        x = self.conv(torch.cat((x1, x2), 1))
        x = x + torch.cat((x1, x2), dim=1)
        return x



func = Model().to('cpu')


x1 = torch.randn(3, 1, 8, 8)

x2 = torch.randn(3, 1, 8, 8)

x3 = torch.randn(3, 1, 8, 8)

test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [1, 1, 3, 3], expected input[3, 2, 8, 8] to have 1 channels, but got 2 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x76ea76196ec0>(*(FakeTensor(..., size=(3, 2, 8, 8)), Parameter(FakeTensor(..., size=(1, 1, 3, 3), requires_grad=True)), Parameter(FakeTensor(..., size=(1,), requires_grad=True)), (1, 1), (1, 1), (1, 1), 1), **{}):
Given groups=1, weight of size [1, 1, 3, 3], expected input[3, 2, 8, 8] to have 1 channels, but got 2 channels instead

from user code:
   File "<string>", line 23, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''