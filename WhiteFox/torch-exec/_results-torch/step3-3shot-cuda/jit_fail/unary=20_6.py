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
        self.conv2 = torch.nn.ConvTranspose2d(3, 8, 1, stride=7, padding=-2)

    def forward(self, x1):
        v1 = self.conv2(x1)
        v2 = torch.sigmoid(v1)
        return v2



func = Model().to('cuda')


x1 = torch.randn(1, 3, 192, 192)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
negative padding is not supported

jit:
Failed running call_function <built-in method conv_transpose2d of type object at 0x782b0a596ec0>(*(FakeTensor(..., device='cuda:0', size=(1, s0, s1, s2)), Parameter(FakeTensor(..., device='cuda:0', size=(3, 8, 1, 1), requires_grad=True)), Parameter(FakeTensor(..., device='cuda:0', size=(8,), requires_grad=True)), (7, 7), (-2, -2), (0, 0), 1, (1, 1)), **{}):
negative padding is not supported

from user code:
   File "<string>", line 20, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 1162, in forward
    return F.conv_transpose2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''