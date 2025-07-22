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

    def __init__(self, negative_slope):
        super().__init__()
        self.conv_t1 = torch.nn.ConvTranspose1d(2, 3, 1, stride=1, padding=0)
        self.conv_t2 = torch.nn.ConvTranspose1d(3, 4, 1, stride=1, padding=0)
        self.negative_slope = negative_slope

    def forward(self, x1):
        t1 = self.conv_t1(x1)
        t2 = self.conv_t2(t1)
        t3 = t2 > 0
        t4 = t2 * self.negative_slope
        t5 = torch.where(t3, t2, t4)
        return t5


negative_slope = -0.1

func = Model(negative_slope).to('cpu')


x = torch.randn(2, 2, 1, 1)

test_inputs = [x]

# JIT_FAIL
'''
direct:
Expected 2D (unbatched) or 3D (batched) input to conv_transpose1d, but got input of size: [2, 2, 1, 1]

jit:
Failed running call_function <built-in method conv_transpose1d of type object at 0x79a54fb96ec0>(*(FakeTensor(..., size=(2, 2, 1, 1)), Parameter(FakeTensor(..., size=(2, 3, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(3,), requires_grad=True)), (1,), (0,), (0,), 1, (1,)), **{}):
Expected 2D (unbatched) or 3D (batched) input to conv_transpose1d, but got input of size: [2, 2, 1, 1]

from user code:
   File "<string>", line 22, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 974, in forward
    return F.conv_transpose1d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''