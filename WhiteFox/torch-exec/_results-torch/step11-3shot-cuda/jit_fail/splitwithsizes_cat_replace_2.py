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
        self.features1 = torch.nn.Sequential(torch.nn.Conv2d(3, 32, 3, 1, 1), torch.nn.MaxPool2d(3, 1, 1, 0))
        self.features2 = torch.nn.Sequential(torch.nn.Conv2d(3, 32, 3, 1, 1))
        self.features = torch.nn.Sequential(self.features1, self.features2)
        self.fc1 = torch.nn.Linear(32, 32)
        self.fc2 = torch.nn.Linear(32, 32)
        self.fc3 = torch.nn.Linear(32, 3)

    def forward(self, x1):
        split_tensors = torch.split(self.features(x1), [1, 1, 1], dim=1)
        concatenated_tensor = torch.cat(split_tensors, dim=1)
        v1 = self.fc1(concatenated_tensor)
        v2 = self.fc2(v1)
        output = self.fc3(v2)
        return (concatenated_tensor, output)



func = Model().to('cuda')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
pad should be at most half of effective kernel size, but got pad=1, kernel_size=3 and dilation=0

jit:
Failed running call_function <function boolean_dispatch.<locals>.fn at 0x7e2b480a2ee0>(*(FakeTensor(..., device='cuda:0', size=(1, 32, 64, 64)), 3, 1, 1, 0), **{'ceil_mode': False, 'return_indices': False}):
pad should be at most half of effective kernel size, but got pad=1, kernel_size=3 and dilation=0

from user code:
   File "<string>", line 25, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/container.py", line 250, in forward
    input = module(input)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/container.py", line 250, in forward
    input = module(input)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/pooling.py", line 213, in forward
    return F.max_pool2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''