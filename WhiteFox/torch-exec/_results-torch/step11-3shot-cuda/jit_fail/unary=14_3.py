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
        self.convtranspose = torch.nn.ConvTranspose2d(3, 8, 5, stride=5)

    def forward(self, x1):
        v1 = self.convtranspose(x1)
        v2 = torch.sigmoid(v1)
        v3 = v1 * v2
        return v3



func = Model().to('cuda')


x1 = torch.randn(1, 32, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [3, 8, 5, 5], expected input[1, 32, 64, 64] to have 3 channels, but got 32 channels instead

jit:
Failed running call_function <built-in method conv_transpose2d of type object at 0x7bebb3196ec0>(*(FakeTensor(..., device='cuda:0', size=(1, s0, s1, s2)), Parameter(FakeTensor(..., device='cuda:0', size=(3, 8, 5, 5), requires_grad=True)), Parameter(FakeTensor(..., device='cuda:0', size=(8,), requires_grad=True)), (5, 5), (0, 0), (0, 0), 1, (1, 1)), **{}):
Given transposed=1, weight of size [3, 8, 5, 5], expected input[1, s0, s1, s2] to have 3 channels, but got s0 channels instead

from user code:
   File "<string>", line 20, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 1162, in forward
    return F.conv_transpose2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''