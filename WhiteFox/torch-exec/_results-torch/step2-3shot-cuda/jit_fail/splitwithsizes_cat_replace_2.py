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
        self.convs = torch.nn.ModuleList([torch.nn.Conv2d(3, 8, 3, stride=2, padding=1), torch.nn.Conv2d(8, 8, 3, stride=1, padding=1)])

    def forward(self, x1):
        for conv in self.convs:
            x1 = conv(x1)
        (split_tensor1, split_tensor2) = torch.split(x1, [32, 48], dim=1)
        x2 = torch.cat((split_tensor1, split_tensor2), dim=1)
        x3 = torch.max(x1, dim=1)[0]
        return True


func = Model().to('cuda')


x1 = torch.randn(1, 128, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [8, 3, 3, 3], expected input[1, 128, 64, 64] to have 3 channels, but got 128 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x7695f1796ec0>(*(FakeTensor(..., device='cuda:0', size=(1, 128, 64, 64)), Parameter(FakeTensor(..., device='cuda:0', size=(8, 3, 3, 3), requires_grad=True)), Parameter(FakeTensor(..., device='cuda:0', size=(8,), requires_grad=True)), (2, 2), (1, 1), (1, 1), 1), **{}):
Given groups=1, weight of size [8, 3, 3, 3], expected input[1, 128, 64, 64] to have 3 channels, but got 128 channels instead

from user code:
   File "<string>", line 21, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''