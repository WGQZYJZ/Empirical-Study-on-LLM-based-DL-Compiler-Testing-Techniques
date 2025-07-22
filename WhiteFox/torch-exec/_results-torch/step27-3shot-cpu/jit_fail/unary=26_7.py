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

    def __init__(self, channels_in):
        super().__init__()
        self.conv_t = torch.nn.ConvTranspose2d(1, 3, 11, padding=5, bias=False)

    def forward(self, x):
        x = self.conv_t(x)
        return x


channels_in = 9

func = Model(channels_in).to('cpu')


channels_in = 9
x = torch.randn(1, channels_in, 12, 12)

test_inputs = [x]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [1, 3, 11, 11], expected input[1, 9, 12, 12] to have 1 channels, but got 9 channels instead

jit:
Failed running call_function <built-in method conv_transpose2d of type object at 0x736832996ec0>(*(FakeTensor(..., size=(1, s0, s1, s2)), Parameter(FakeTensor(..., size=(1, 3, 11, 11), requires_grad=True)), None, (1, 1), (5, 5), (0, 0), 1, (1, 1)), **{}):
Given transposed=1, weight of size [1, 3, 11, 11], expected input[1, s0, s1, s2] to have 1 channels, but got s0 channels instead

from user code:
   File "<string>", line 20, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 1162, in forward
    return F.conv_transpose2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''