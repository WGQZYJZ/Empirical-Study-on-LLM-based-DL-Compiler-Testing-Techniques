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

class Model(nn.Module):

    def __init__(self):
        super().__init__()
        self.layers = nn.Linear(2, 2)

    def forward(self, x):
        x = torch.cat([x, x], dim=1)
        return x

class MyModel(nn.Module):

    def __init__(self):
        super(MyModel, self).__init__()
        self.conv_1d = nn.Conv1d(1, 16, kernel_size=1, stride=1)
        self.conv_2d = nn.Conv2d(16, 1, kernel_size=1, stride=1)

    def forward(input):
        x = self.conv_1d(input)
        return self.conv_2d(x)

class Model(nn.Module):

    def __init__(self):
        super(Model, self).__init__()

    def forward(x):
        x = torch.cat((x, x), dim=1)
        x = torch.stack((x, x), dim=1)
        return x

class MyModel(nn.Module):

    def __init__(self):
        super(MyModel, self).__init__()
        self.conv_1d = nn.Conv1d(1, 16, kernel_size=1)
        self.conv_2d = nn.Conv2d(16, 1, kernel_size=1)

    def forward(input):
        x = self.conv_1d(input)
        return self.conv_2d(x)

class Model(nn.Module):

    def __init__(self):
        super(Model, self).__init__()

    def forward(x):
        x = torch.cat((x, x), dim=1)
        return x

class Model(nn.Module):

    def __init__(self):
        super(Model, self).__init__()
        self.layers = nn.Linear(2, 4)

    def forward(x):
        x = self.layers(x)
        x = torch.cat((x, x), dim=1)
        return x

class Model(nn.Module):

    def __init__(self):
        super(Model, self).__init__()
        self.layers1 = nn.Sequential(nn.Conv2d(3, 16, 3, padding=1), nn.AvgPool2d(2, 2))
        self.layers2 = nn.Sequential(nn.Conv2d(16, 32, 3, padding=1), nn.AvgPool2d(2, 2))
        self.fc = nn.Linear(32 * 4 * 4, 84)

    def forward(self, x):
        out1 = self.layers1(x)
        out2 = self.layers2(out1)
        out3 = out2.view(out2.size(0), -1)
        out4 = self.fc(out3)
        return out4



func = Model().to('cpu')


x = torch.randn(2, 2)

test_inputs = [x]

# JIT_FAIL
'''
direct:
Expected 3D (unbatched) or 4D (batched) input to conv2d, but got input of size: [2, 2]

jit:
Failed running call_function <built-in method conv2d of type object at 0x747e85596ec0>(*(FakeTensor(..., size=(2, 2)), Parameter(FakeTensor(..., size=(16, 3, 3, 3), requires_grad=True)), Parameter(FakeTensor(..., size=(16,), requires_grad=True)), (1, 1), (1, 1), (1, 1), 1), **{}):
Expected 3D (unbatched) or 4D (batched) input to conv2d, but got input of size: [2, 2]

from user code:
   File "<string>", line 84, in forward
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