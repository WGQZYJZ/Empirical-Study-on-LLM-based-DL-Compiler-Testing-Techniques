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
        self.linear = torch.nn.Linear(2800, 800)
        self.conv1 = torch.nn.Conv1d(in_channels=10, out_channels=10, kernel_size=(1,))
        self.conv2 = torch.nn.Conv1d(in_channels=10, out_channels=10, kernel_size=(1,))

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        v3 = v2.unsqueeze(1)
        v4 = self.conv2(v3)
        v5 = v4.squeeze(1)
        v6 = self.conv1(v1)
        x2 = v5 + v6
        return x2



func = Model().to('cpu')


x1 = torch.randn(1, 2800, 10)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected 2D (unbatched) or 3D (batched) input to conv1d, but got input of size: [1, 1, 10, 800]

jit:
Failed running call_function <built-in method conv1d of type object at 0x7c9959196ec0>(*(FakeTensor(..., size=(1, 1, 10, 800)), Parameter(FakeTensor(..., size=(10, 10, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(10,), requires_grad=True)), (1,), (0,), (1,), 1), **{}):
Expected 2D (unbatched) or 3D (batched) input to conv1d, but got input of size: [1, 1, 10, 800]

from user code:
   File "<string>", line 25, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 375, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 370, in _conv_forward
    return F.conv1d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''