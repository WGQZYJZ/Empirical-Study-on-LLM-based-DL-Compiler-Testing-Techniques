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
        self.features = torch.nn.Sequential(*[torch.nn.Conv2d(3, 10, kernel_size=5), torch.nn.ReLU(), torch.nn.MaxPool2d(kernel_size=2, stride=2, return_indices=not bool()), torch.nn.Conv2d(10, 20, kernel_size=5), torch.nn.ReLU(), torch.nn.MaxPool2d(kernel_size=2, stride=2, return_indices=not bool()), torch.nn.ReLU()]).eval()

    def forward(self, x):
        t1 = torch.cat([x, x], dim=1)
        t2 = t1.tanh()
        t3 = self.features(t2)
        y = t3
        return y



func = Model().to('cpu')


x = torch.randn(2, 3, 10, 10)

test_inputs = [x]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [10, 3, 5, 5], expected input[2, 6, 10, 10] to have 3 channels, but got 6 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x745abe196ec0>(*(FakeTensor(..., size=(2, 6, 10, 10)), Parameter(FakeTensor(..., size=(10, 3, 5, 5), requires_grad=True)), Parameter(FakeTensor(..., size=(10,), requires_grad=True)), (1, 1), (0, 0), (1, 1), 1), **{}):
Given groups=1, weight of size [10, 3, 5, 5], expected input[2, 6, 10, 10] to have 3 channels, but got 6 channels instead

from user code:
   File "<string>", line 22, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/container.py", line 250, in forward
    input = module(input)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''