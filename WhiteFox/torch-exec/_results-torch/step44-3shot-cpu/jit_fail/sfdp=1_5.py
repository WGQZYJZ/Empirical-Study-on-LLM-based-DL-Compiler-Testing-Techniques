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
        self.dropout = torch.nn.Dropout(0.2)
        self.conv1 = torch.nn.Conv2d(in_channels=3, out_channels=16, kernel_size=3, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(in_channels=16, out_channels=8, kernel_size=3, stride=2, padding=1)
        self.conv3 = torch.nn.Conv2d(in_channels=8, out_channels=4, kernel_size=3, stride=4, padding=1)
        self.lin1 = torch.nn.Linear(in_features=704, out_features=64)
        self.lin2 = torch.nn.Linear(in_features=64, out_features=128)
        self.lin3 = torch.nn.Linear(in_features=128, out_features=32)
        self.lin4 = torch.nn.Linear(in_features=32, out_features=256)
        self.conv = torch.nn.Conv2d(2304, 384, 1, stride=1, padding=1)
        self.conv2d = torch.nn.Conv2d(256, 256, 3, stride=1, padding=1)

    def forward(self, x):
        x_conv1 = F.relu(self.conv1(x))
        x_conv2 = F.relu(self.conv2(x_conv1))
        x_conv3 = F.relu(self.conv3(x_conv2))
        x_lin = F.relu(self.lin1(x_conv3.view(x_conv3.size(0), -1)))
        x_lin2 = F.relu(self.lin2(x_lin))
        x_lin3 = F.relu(self.lin3(x_lin2))
        x_lin4 = F.relu(self.lin4(x_lin3))
        x_cat = torch.cat([x_conv3, x_lin4], dim=1)
        x_conv = F.relu(self.conv(x_cat))
        x_conv2d = F.relu(self.conv2d(x_conv))
        return x_conv2d


func = Model().to('cpu')


x = torch.randn(1, 3, 32, 64)

test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x128 and 704x64)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 128)), Parameter(FakeTensor(..., size=(64, 704), requires_grad=True)), Parameter(FakeTensor(..., size=(64,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [1, 128] X [704, 64].

from user code:
   File "<string>", line 32, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''