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
        self.conv1 = torch.nn.Conv2d(in_channels=12, out_channels=104, kernel_size=(1, 11), stride=(1, 1), padding=(0, 6))
        self.conv2 = torch.nn.Conv2d(104, 4, kernel_size=(1, 7), stride=(1, 1), padding=(0, 2))
        self.conv3 = torch.nn.ConvTranspose2d(4, 2, kernel_size=(1, 7), stride=(1, 1), padding=(0, 2))
        self.conv4 = torch.nn.Conv2d(2, 250, kernel_size=(14, 1), stride=(1, 1), padding=(0, 0))
        self.conv5 = torch.nn.Conv2d(250, 168, kernel_size=(1, 1), stride=(1, 1), padding=(0, 0))
        self.conv6 = torch.nn.Conv2d(168, 250, kernel_size=(5, 1), stride=(1, 1), padding=(2, 0))
        self.conv7 = torch.nn.Conv2d(250, 510, kernel_size=(1, 1), stride=(1, 1), padding=(0, 0))
        self.conv8 = torch.nn.Conv2d(510, 129, kernel_size=(1, 1), stride=(1, 1), padding=(0, 0))

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = torch.sigmoid(v1)
        v3 = torch.nn.functional.avg_pool2d(v2, (1, 3), stride=(1, 3), padding=(0, 1))
        v4 = self.conv2(v3)
        v5 = torch.sigmoid(v4)
        v6 = self.conv3(v5)
        v7 = torch.sigmoid(v6)
        v8 = torch.nn.functional.avg_pool2d(v7, (15, 2), stride=(15, 2), padding=(0, 0))
        v9 = self.conv4(v8)
        v10 = torch.functional.max_pool2d(v9, (3, 1), stride=(3, 1), padding=(1, 0))
        v11 = self.conv5(v10)
        v12 = torch.functional.max_pool2d(v11, (1, 1), stride=(1, 1), padding=(0, 0))
        v13 = torch.functional.max_pool2d(v12, (1, 1), stride=(1, 1), padding=(0, 0))
        v14 = self.conv6(v13)
        v15 = torch.functional.max_pool2d(v14, (1, 1), stride=(1, 1), padding=(0, 0))
        v16 = self.conv7(v15)
        v17 = torch.functional.max_pool2d(v16, (1, 1), stride=(1, 1), padding=(0, 0))
        v18 = self.conv8(v17)
        return v18



func = Model().to('cpu')


x1 = torch.randn(1, 12, 15, 80)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (1 x 14). Kernel size: (14 x 1). Kernel size can't be greater than actual input size

jit:
Failed running call_function <built-in method conv2d of type object at 0x707b51f96ec0>(*(FakeTensor(..., size=(1, 2, 1, 14)), Parameter(FakeTensor(..., size=(250, 2, 14, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(250,), requires_grad=True)), (1, 1), (0, 0), (1, 1), 1), **{}):
Calculated padded input size per channel: (1 x 14). Kernel size: (14 x 1). Kernel size can't be greater than actual input size

from user code:
   File "<string>", line 35, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''