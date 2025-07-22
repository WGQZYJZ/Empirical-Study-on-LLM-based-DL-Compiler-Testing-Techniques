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

class ModelTanh(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv2d = torch.nn.Conv2d(16, 63, 1, stride=1)
        self.conv1d = torch.nn.Conv1d(16, 125, 1, stride=1)

    def forward(self, x0):
        v1 = self.conv2d(x0)
        v2 = torch.tanh(v1)
        v3 = self.conv1d(v2)
        return torch.tanh(v3)



func = ModelTanh().to('cpu')


x0 = torch.randn(32, 16, 199, 299)

test_inputs = [x0]

# JIT_FAIL
'''
direct:
Expected 2D (unbatched) or 3D (batched) input to conv1d, but got input of size: [32, 63, 199, 299]

jit:
Failed running call_function <built-in method conv1d of type object at 0x74746f196ec0>(*(FakeTensor(..., size=(32, 63, 199, 299)), Parameter(FakeTensor(..., size=(125, 16, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(125,), requires_grad=True)), (1,), (0,), (1,), 1), **{}):
Expected 2D (unbatched) or 3D (batched) input to conv1d, but got input of size: [32, 63, 199, 299]

from user code:
   File "<string>", line 23, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 375, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 370, in _conv_forward
    return F.conv1d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''