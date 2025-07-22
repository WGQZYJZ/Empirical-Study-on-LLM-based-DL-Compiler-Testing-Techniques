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
        self.linear = torch.nn.Conv2d(2, 2, 2)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.nn.functional.conv2d(v1, self.linear.weight, bias=self.linear.bias, stride=self.linear.stride, padding=self.linear.padding, dilation=self.linear.dilation, groups=self.linear.groups)
        return v2.reshape([1, 2, 2, 2])




func = Model().to('cuda')



x1 = torch.randn(1, 2, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [2, 2, 2, 2], expected input[1, 1, 2, 2] to have 2 channels, but got 1 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x72c26b8699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 2, 2)), Parameter(FakeTensor(..., device='cuda:0', size=(2, 2, 2, 2), requires_grad=True))), **{'bias': Parameter(FakeTensor(..., device='cuda:0', size=(2,), requires_grad=True)), 'stride': (1, 1), 'padding': (0, 0), 'dilation': (1, 1), 'groups': 1}):
Given groups=1, weight of size [2, 2, 2, 2], expected input[1, 1, 2, 2] to have 2 channels, but got 1 channels instead

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''