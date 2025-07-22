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
        self.conv_block = torch.nn.Sequential(torch.nn.Conv2d(3, 32, kernel_size=3, stride=1, padding=1), torch.nn.ReLU(), torch.nn.MaxPool2d(2, 2), torch.nn.Conv2d(32, 64, kernel_size=3, stride=1, padding=1), torch.nn.ReLU(), torch.nn.MaxPool2d(2, 3), torch.nn.Conv2d(64, 64, kernel_size=3, stride=1, padding=1), torch.nn.ReLU(), torch.nn.MaxPool2d(2, 2), torch.nn.Conv2d(64, 128, kernel_size=3, stride=1, padding=1), torch.nn.ReLU(), torch.nn.MaxPool2d(2, 2))
        self.fc = torch.nn.Sequential(torch.nn.Linear(128 * 38 * 38, 256), torch.nn.ReLU(), torch.nn.Linear(256, 128), torch.nn.ReLU(), torch.nn.Linear(128, 2))

    def forward(self, x1):
        v1 = self.conv_block(x1)
        v2 = v1.reshape(v1.size(0), -1)
        v3 = self.fc(v2)
        return v3



func = Model().to('cpu')


x1 = torch.randn(1, 3, 300, 300)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x18432 and 184832x256)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(...,
           size=(1, 128*((((((((((((s1//2)) - 2)//3)) - 1)//2)) - 1)//2)) + 1)*((((((((((((s2//2)) - 2)//3)) - 1)//2)) - 1)//2)) + 1))), Parameter(FakeTensor(..., size=(256, 184832), requires_grad=True)), Parameter(FakeTensor(..., size=(256,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [1, 128*((((((((((((s1//2)) - 2)//3)) - 1)//2)) - 1)//2)) + 1)*((((((((((((s2//2)) - 2)//3)) - 1)//2)) - 1)//2)) + 1)] X [184832, 256].

from user code:
   File "<string>", line 23, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/container.py", line 250, in forward
    input = module(input)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''