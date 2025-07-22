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
        self.features = torch.nn.Sequential(torch.nn.Conv2d(3, 32, 3, 1, 1), torch.nn.ReLU(inplace=False), torch.nn.Conv2d(32, 32, 3, 1, 1))
        self.concat = torch.nn.Sequential(torch.nn.Conv2d(32, 32, 3, 1, 0))
        self.features_1 = torch.nn.Sequential(torch.nn.Conv2d(32, 32, 3, 1, 2))
        self.features_2 = torch.nn.Sequential(torch.nn.Conv2d(32, 32, 1, 2), torch.nn.ReLU(inplace=True))

    def forward(self, v1):
        split_tensors = torch.split(v1, [1, 1, 1], dim=1)
        concatenated_tensor = torch.cat(split_tensors, dim=1)
        (intermediate, _) = self.features_1(split_tensors[1])
        (intermediate, _) = self.features_2(intermediate)
        (_, split) = self.features(split_tensors[1])
        return (concatenated_tensor, torch.split(v1, [1, 1, 1], dim=1), intermediate, split)



func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [32, 32, 3, 3], expected input[1, 1, 64, 64] to have 32 channels, but got 1 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x79f50df96ec0>(*(FakeTensor(..., size=(1, 1, 64, 64)), Parameter(FakeTensor(..., size=(32, 32, 3, 3), requires_grad=True)), Parameter(FakeTensor(..., size=(32,), requires_grad=True)), (1, 1), (2, 2), (1, 1), 1), **{}):
Given groups=1, weight of size [32, 32, 3, 3], expected input[1, 1, 64, 64] to have 32 channels, but got 1 channels instead

from user code:
   File "<string>", line 25, in forward
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