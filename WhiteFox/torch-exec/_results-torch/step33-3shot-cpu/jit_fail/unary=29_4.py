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

    def __init__(self, min_value=-1.9282, max_value=9.416):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(8, 5, 1, stride=1, padding=0)
        self.conv_transpose = torch.nn.ConvTranspose1d(10, 7, 5, stride=1, padding=1)
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = torch.clamp_min(v1, self.min_value)
        v3 = torch.clamp_max(v2, self.max_value)
        return v3



func = Model().to('cpu')


x1 = torch.randn(1, 8, 137, 123)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected 2D (unbatched) or 3D (batched) input to conv_transpose1d, but got input of size: [1, 8, 137, 123]

jit:
Failed running call_function <built-in method conv_transpose1d of type object at 0x7349ead96ec0>(*(FakeTensor(..., size=(1, 8, 137, 123)), Parameter(FakeTensor(..., size=(10, 7, 5), requires_grad=True)), Parameter(FakeTensor(..., size=(7,), requires_grad=True)), (1,), (1,), (0,), 1, (1,)), **{}):
Expected 2D (unbatched) or 3D (batched) input to conv_transpose1d, but got input of size: [1, 8, 137, 123]

from user code:
   File "<string>", line 23, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 974, in forward
    return F.conv_transpose1d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''