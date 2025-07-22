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
        self.conv = torch.nn.Conv2d(3, 47, (7, 11), stride=(4, 5), padding=(2, 2))
        self.conv2 = torch.nn.Conv2d(47, 55, (8, 12), stride=(4, 12), padding=(1, 3))
        self.conv3 = torch.nn.Conv2d(55, 39, (3, 8), stride=(3, 5), padding=(0, 4))
        self.conv4 = torch.nn.Conv2d(39, 50, (4, 13), stride=(5, 14), padding=(0, 2))

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5
        v7 = self.conv2(v6)
        v8 = v7 * 0.5
        v9 = v7 * 0.7071067811865476
        v10 = torch.erf(v9)
        v11 = v10 + 1
        v12 = v8 * v11
        v13 = self.conv3(v12)
        v14 = v7 * 0.5
        v15 = v7 * 0.7071067811865476
        v16 = torch.erf(v15)
        v17 = v16 + 1
        v18 = v14 * v17
        v19 = self.conv4(v18)
        v20 = v19 * 0.5
        v21 = v19 * 0.7071067811865476
        v22 = torch.erf(v21)
        v23 = v22 + 1
        v24 = v20 * v23
        return v24



func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 3004)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [50, 39, 4, 13], expected input[1, 55, 3, 50] to have 39 channels, but got 55 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x70f3d7596ec0>(*(FakeTensor(...,
           size=(1, 55, ((((((s1 - 3)//4)) - 5)//4)) + 1, ((((((s2 - 7)//5)) - 5)//12)) + 1)), Parameter(FakeTensor(..., size=(50, 39, 4, 13), requires_grad=True)), Parameter(FakeTensor(..., size=(50,), requires_grad=True)), (5, 14), (0, 2), (1, 1), 1), **{}):
Given groups=1, weight of size [50, 39, 4, 13], expected input[1, 55, ((((((s1 - 3)//4)) - 5)//4)) + 1, ((((((s2 - 7)//5)) - 5)//12)) + 1] to have 39 channels, but got 55 channels instead

from user code:
   File "<string>", line 41, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''