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

    def __init__(self, min_value=1.0, max_value=7.83):
        super().__init__()
        self.sigmoid = torch.nn.Sigmoid()
        self.leaky_relu = torch.nn.LeakyReLU()
        self.avg_pool2d = torch.nn.AvgPool2d(kernel_size=1)
        self.max_pool2d = torch.nn.MaxPool2d(kernel_size=1, stride=1, padding=1)
        self.conv2d_1 = torch.nn.Conv2d(3, 5, (5, 11))
        self.conv2d_2 = torch.nn.Conv2d(159, 6, (10, 7))
        self.conv_transpose_1 = torch.nn.ConvTranspose2d(60, 37, (4, 3), (2, 2), (1, 1))
        self.conv2d_3 = torch.nn.Conv2d(37, 7, 5)
        self.conv_transpose_2 = torch.nn.ConvTranspose2d(7, 29, 5, (2, 1), 1)
        self.conv2d_4 = torch.nn.Conv2d(29, 10, 3, 2, 1)
        self.conv_transpose_3 = torch.nn.ConvTranspose2d(10, 5, 3, 2, 1)
        self.conv_transpose_4 = torch.nn.ConvTranspose2d(5, 81, 1, (1, 1))
        self.relu = torch.nn.ReLU()
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x):
        v1 = self.conv_transpose_1(x)
        v2 = self.conv2d_1(v1)
        v3 = self.max_pool2d(v2)
        v4 = self.conv2d_2(v3)
        v5 = self.conv_transpose_2(v4)
        v6 = self.avg_pool2d(v5)
        v18 = torch.cat([v1.flatten(1), v6], 1)
        v7 = self.conv2d_3(v18)
        v8 = self.conv_transpose_3(v7)
        v9 = self.conv2d_4(v8)
        v10 = self.conv_transpose_4(v9)
        v11 = self.avg_pool2d(v10)
        v12 = self.relu(v11)
        v13 = self.conv2d_2(v12)
        v14 = self.max_pool2d(v13)
        v15 = self.conv2d_3(v14)
        v16 = self.conv_transpose_3(v15)
        v17 = self.avg_pool2d(v16)
        return torch.flatten(v17, start_dim=1)



func = Model().to('cpu')


x = torch.randn(1, 81, 5, 5)

test_inputs = [x]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [60, 37, 4, 3], expected input[1, 81, 5, 5] to have 60 channels, but got 81 channels instead

jit:
Failed running call_function <built-in method conv_transpose2d of type object at 0x7cb272d96ec0>(*(FakeTensor(..., size=(1, 81, 5, 5)), Parameter(FakeTensor(..., size=(60, 37, 4, 3), requires_grad=True)), Parameter(FakeTensor(..., size=(37,), requires_grad=True)), (2, 2), (1, 1), (0, 0), 1, (1, 1)), **{}):
Given transposed=1, weight of size [60, 37, 4, 3], expected input[1, 81, 5, 5] to have 60 channels, but got 81 channels instead

from user code:
   File "<string>", line 34, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 1162, in forward
    return F.conv_transpose2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''