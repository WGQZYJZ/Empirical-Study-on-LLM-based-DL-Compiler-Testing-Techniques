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
        self.linear1 = torch.nn.Linear(10, 10)
        self.conv2d = torch.nn.Conv2d(10, 10, 2, padding=0, stride=1, dilation=1, groups=1)
        self.gelu = torch.nn.GELU()
        self.linear2 = torch.nn.Linear(10, 5)

    def forward(self, x38):
        v38 = self.gelu(x38)
        x39 = v38.transpose(0, 1)
        v39 = self.conv2d(x39)
        v40 = v39.transpose(0, 2)
        v41 = v40.reshape(10, 5)
        v42 = v40.permute(0, 1, 3, 2).contiguous().reshape(-1, 5)
        x41 = self.linear2(v42)
        v43 = self.linear1(v38)
        x41 = x41.view(1, -1, 5)
        v44 = torch.mean(x41, dim=[1, 2]).transpose(1, 0)
        v45 = torch.sum(v43, -1).reshape(5, 1)
        x42 = x38 + v40
        return v45



func = Model().to('cpu')


x38 = torch.randn(5, 10)

test_inputs = [x38]

# JIT_FAIL
'''
direct:
Expected 3D (unbatched) or 4D (batched) input to conv2d, but got input of size: [10, 5]

jit:
Failed running call_function <built-in method conv2d of type object at 0x70b2fff96ec0>(*(FakeTensor(..., size=(10, 5)), Parameter(FakeTensor(..., size=(10, 10, 2, 2), requires_grad=True)), Parameter(FakeTensor(..., size=(10,), requires_grad=True)), (1, 1), (0, 0), (1, 1), 1), **{}):
Expected 3D (unbatched) or 4D (batched) input to conv2d, but got input of size: [10, 5]

from user code:
   File "<string>", line 25, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''