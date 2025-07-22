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

    def __init__(self, min_value=17103715, max_value=184578103):
        super().__init__()
        self.min_value = min_value
        self.max_value = max_value
        self.conv_transpose2d = torch.nn.ConvTranspose2d(3, 64, kernel_size=(2, 2), stride=(2, 2), padding=(1, 1))
        self.conv2d = torch.nn.Conv2d(64, 256, kernel_size=(3, 3), stride=(2, 2), padding=(1, 1))
        self.conv_transpose3d = torch.nn.ConvTranspose3d(256, 3, kernel_size=(4, 3, 2), stride=(3, 1, 5), padding=(1, 0, 5))
        self.tanh = torch.nn.Tanh()
        self.max_pool3d = torch.nn.MaxPool3d(kernel_size=2, stride=1, padding=1)
        self.max_pool2d = torch.nn.MaxPool2d(kernel_size=1, stride=1, padding=0)
        self.avg_pool2d = torch.nn.AvgPool2d(kernel_size=1, stride=1, padding=0)

    def forward(self, x):
        v1 = torch.clamp_min(self.conv_transpose2d(x), self.min_value)
        v2 = torch.clamp_max(v1, self.max_value)
        v7 = self.conv2d(v2)
        v6 = torch.clamp_min(v7, self.min_value)
        v8 = torch.clamp_max(v6, self.max_value)
        v9 = self.conv_transpose3d(v8)
        v11 = self.tanh(v9)
        v3 = torch.clamp_min(v11, self.min_value)
        v4 = torch.clamp_max(v3, self.min_value)
        v10 = self.max_pool3d(v4)
        v5 = torch.clamp_min(v10, self.max_value)
        v12 = self.max_pool2d(v5)
        v13 = self.tanh(v12)
        v14 = self.avg_pool2d(v13)
        return v14



func = Model().to('cpu')


x1 = torch.randn(1, 3, 108, 7, 7)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected 3D (unbatched) or 4D (batched) input to conv_transpose2d, but got input of size: [1, 3, 108, 7, 7]

jit:
Failed running call_function <built-in method conv_transpose2d of type object at 0x7f4da7396ec0>(*(FakeTensor(..., size=(1, 3, 108, 7, 7)), Parameter(FakeTensor(..., size=(3, 64, 2, 2), requires_grad=True)), Parameter(FakeTensor(..., size=(64,), requires_grad=True)), (2, 2), (1, 1), (0, 0), 1, (1, 1)), **{}):
Expected 3D (unbatched) or 4D (batched) input to conv_transpose2d, but got input of size: [1, 3, 108, 7, 7]

from user code:
   File "<string>", line 28, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 1162, in forward
    return F.conv_transpose2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''