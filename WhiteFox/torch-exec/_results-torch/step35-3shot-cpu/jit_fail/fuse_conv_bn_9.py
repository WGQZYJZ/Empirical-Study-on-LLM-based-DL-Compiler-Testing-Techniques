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
        torch.manual_seed(1)
        self.conv = torch.nn.Conv2d(3, 3, 3)
        torch.manual_seed(1)
        self.layernorm = torch.nn.LayerNorm(3)

    def forward(self, x2):
        x = self.conv(x2)
        y = self.layernorm(x)
        return y



func = Model().to('cpu')


x2 = torch.randn(1, 3, 6, 6)

test_inputs = [x2]

# JIT_FAIL
'''
direct:
Given normalized_shape=[3], expected input with shape [*, 3], but got input of size[1, 3, 4, 4]

jit:
Failed running call_function <function layer_norm at 0x73c7fdcaf040>(*(FakeTensor(..., size=(1, 3, 4, 4)), (3,), Parameter(FakeTensor(..., size=(3,), requires_grad=True)), Parameter(FakeTensor(..., size=(3,), requires_grad=True)), 1e-05), **{}):
Given normalized_shape=[3], expected input with shape [3], but got input of size torch.Size([1, 3, 4, 4])

from user code:
   File "<string>", line 24, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/normalization.py", line 217, in forward
    return F.layer_norm(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''