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
        self.conv = torch.nn.Conv1d(1, 1, kernel_size=(1,), stride=(1,), padding=(0,), dilation=1, groups=1, bias=False)

    def forward(self, x):
        v1 = self.conv(x)
        v2 = v1 - x
        return v2



func = Model().to('cpu')


x = torch.randn(1, 1, 64, 64)

test_inputs = [x]

# JIT_FAIL
'''
direct:
Expected 2D (unbatched) or 3D (batched) input to conv1d, but got input of size: [1, 1, 64, 64]

jit:
Failed running call_function <built-in method conv1d of type object at 0x70c18e596ec0>(*(FakeTensor(..., size=(1, 1, 64, 64)), Parameter(FakeTensor(..., size=(1, 1, 1), requires_grad=True)), None, (1,), (0,), (1,), 1), **{}):
Expected 2D (unbatched) or 3D (batched) input to conv1d, but got input of size: [1, 1, 64, 64]

from user code:
   File "<string>", line 20, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 375, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 370, in _conv_forward
    return F.conv1d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''