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
        self.dense = torch.nn.Linear(16, 16)
        self.conv = torch.nn.Conv2d(16, 16, 3, stride=1, padding=1)

    def forward(self, x):
        v1 = x + self.dense(x)
        v2 = v1 + self.dense(x)
        v3 = v2 + self.conv(x)
        return v3



func = Model().to('cpu')


x = torch.randn(1, 16)

test_inputs = [x]

# JIT_FAIL
'''
direct:
Expected 3D (unbatched) or 4D (batched) input to conv2d, but got input of size: [1, 16]

jit:
Failed running call_function <built-in method conv2d of type object at 0x7f2b88196ec0>(*(FakeTensor(..., size=(1, 16)), Parameter(FakeTensor(..., size=(16, 16, 3, 3), requires_grad=True)), Parameter(FakeTensor(..., size=(16,), requires_grad=True)), (1, 1), (1, 1), (1, 1), 1), **{}):
Expected 3D (unbatched) or 4D (batched) input to conv2d, but got input of size: [1, 16]

from user code:
   File "<string>", line 23, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''