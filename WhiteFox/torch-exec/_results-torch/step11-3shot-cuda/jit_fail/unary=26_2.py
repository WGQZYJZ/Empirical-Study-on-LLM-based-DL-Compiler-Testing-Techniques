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
        self.conv_t = torch.nn.ConvTranspose2d(11, 3, 2, stride=2)
        self.conv_t3 = torch.nn.ConvTranspose3d(22, 44, 3)

    def forward(self, x2):
        x5 = self.conv_t(x2)
        x6 = x5 * 0.578
        x7 = self.conv_t3(x2)
        return (x6, x7)



func = Model().to('cuda')


x2 = torch.randn(3, 11, 8, 8)

test_inputs = [x2]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [22, 44, 3, 3, 3], expected input[1, 3, 11, 8, 8] to have 22 channels, but got 3 channels instead

jit:
Failed running call_function <built-in method conv_transpose3d of type object at 0x7d1179196ec0>(*(FakeTensor(..., device='cuda:0', size=(s0, 11, s2, s3)), Parameter(FakeTensor(..., device='cuda:0', size=(22, 44, 3, 3, 3), requires_grad=True)), Parameter(FakeTensor(..., device='cuda:0', size=(44,), requires_grad=True)), (1, 1, 1), (0, 0, 0), (0, 0, 0), 1, (1, 1, 1)), **{}):
Given transposed=1, weight of size [22, 44, 3, 3, 3], expected input[1, s0, 11, s2, s3] to have 22 channels, but got s0 channels instead

from user code:
   File "<string>", line 23, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 1347, in forward
    return F.conv_transpose3d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''