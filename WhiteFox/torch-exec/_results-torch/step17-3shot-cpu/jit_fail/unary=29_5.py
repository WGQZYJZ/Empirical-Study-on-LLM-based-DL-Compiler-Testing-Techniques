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

    def __init__(self, min_value=0.7, max_value=7.3):
        super().__init__()
        self.softmax = torch.nn.Softmax(12)
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 24, 1, stride=1, padding=1)
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x):
        v1 = self.conv_transpose(x)
        v2 = torch.clamp_min(v1, self.min_value)
        v3 = torch.clamp_max(v2, self.max_value)
        v5 = self.softmax(v3)
        return v5



func = Model().to('cpu')


x = torch.randn(1, 3, 224, 224)

test_inputs = [x]

# JIT_FAIL
'''
direct:
Dimension out of range (expected to be in range of [-4, 3], but got 12)

jit:
Failed running call_function <function softmax at 0x7248829ac700>(*(FakeTensor(..., size=(1, 24, 222, 222)), 12), **{'_stacklevel': 5}):
Dimension out of range (expected to be in range of [-4, 3], but got 12)

from user code:
   File "<string>", line 26, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/activation.py", line 1672, in forward
    return F.softmax(input, self.dim, _stacklevel=5)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''