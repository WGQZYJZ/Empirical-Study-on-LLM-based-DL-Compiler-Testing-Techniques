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
        self.conv1 = torch.nn.Conv2d(1, 3, 3)
        self.conv2 = torch.nn.Conv1d(1, 3, 3)

    def forward(self, x):
        a1 = self.conv1(x)
        a2 = self.conv2(x)
        b1 = a1
        b2 = torch.nn.functional.relu(a1)
        z1 = torch.nn.functional.dropout(b1, p=0.1)
        z2 = torch.nn.functional.dropout(b2, p=0.1)
        o1 = z1 + z2
        return o1



func = Model().to('cpu')


x1 = torch.randn(1, 1, 23, 22)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected 2D (unbatched) or 3D (batched) input to conv1d, but got input of size: [1, 1, 23, 22]

jit:
Failed running call_function <built-in method conv1d of type object at 0x77f786196ec0>(*(FakeTensor(..., size=(1, 1, 23, 22)), Parameter(FakeTensor(..., size=(3, 1, 3), requires_grad=True)), Parameter(FakeTensor(..., size=(3,), requires_grad=True)), (1,), (0,), (1,), 1), **{}):
Expected 2D (unbatched) or 3D (batched) input to conv1d, but got input of size: [1, 1, 23, 22]

from user code:
   File "<string>", line 22, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 375, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 370, in _conv_forward
    return F.conv1d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''