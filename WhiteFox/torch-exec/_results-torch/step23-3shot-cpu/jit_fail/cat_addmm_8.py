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
        self.layers1 = nn.Conv1d(10, 256, kernel_size=1)
        self.layers2 = nn.Conv2d(512, 1024, kernel_size=1)

    def forward(self, x):
        x = self.layers2(self.layers1(x))
        x = x.flatten(start_dim=2)
        x = x.flatten(start_dim=1)
        return x



func = Model().to('cpu')


x = torch.randn(2, 16, 10, 10)

test_inputs = [x]

# JIT_FAIL
'''
direct:
Expected 2D (unbatched) or 3D (batched) input to conv1d, but got input of size: [2, 16, 10, 10]

jit:
Failed running call_function <built-in method conv1d of type object at 0x7fb014596ec0>(*(FakeTensor(..., size=(2, 16, 10, 10)), Parameter(FakeTensor(..., size=(256, 10, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(256,), requires_grad=True)), (1,), (0,), (1,), 1), **{}):
Expected 2D (unbatched) or 3D (batched) input to conv1d, but got input of size: [2, 16, 10, 10]

from user code:
   File "<string>", line 21, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 375, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 370, in _conv_forward
    return F.conv1d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''