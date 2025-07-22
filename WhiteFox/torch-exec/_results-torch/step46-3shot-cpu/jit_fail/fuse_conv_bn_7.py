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
        self.fc = torch.nn.Linear(16, 16)
        self.conv = torch.nn.Conv3d(16, 16, (3, 3, 3))
        self.bn = torch.nn.BatchNorm3d(16)

    def forward(self, x):
        y = self.fc(x)
        y = self.conv(y)
        y = self.bn(y)
        return y



func = Model().to('cpu')


x = torch.randn(1, 16)

test_inputs = [x]

# JIT_FAIL
'''
direct:
Expected 4D (unbatched) or 5D (batched) input to conv3d, but got input of size: [1, 16]

jit:
Failed running call_function <built-in method conv3d of type object at 0x7d7237596ec0>(*(FakeTensor(..., size=(1, 16)), Parameter(FakeTensor(..., size=(16, 16, 3, 3, 3), requires_grad=True)), Parameter(FakeTensor(..., size=(16,), requires_grad=True)), (1, 1, 1), (0, 0, 0), (1, 1, 1), 1), **{}):
Expected 4D (unbatched) or 5D (batched) input to conv3d, but got input of size: [1, 16]

from user code:
   File "<string>", line 23, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 725, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 720, in _conv_forward
    return F.conv3d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''