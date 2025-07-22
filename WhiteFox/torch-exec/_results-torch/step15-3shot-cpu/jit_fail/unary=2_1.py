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
        self.conv_transpose1 = torch.nn.ConvTranspose2d(1, 24, kernel_size=(3, 3), stride=(3, 3), padding=1)
        self.avg_pool = torch.nn.AvgPool2d(kernel_size=(3, 3), stride=(3, 3), padding=2)

    def forward(self, x1):
        v1 = self.conv_transpose1(x1)
        v2 = self.avg_pool(v1)
        return v2



func = Model().to('cpu')


x1 = torch.randn(5, 1, 2, 6)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
pad should be at most half of effective kernel size, but got pad=2, kernel_size=3 and dilation=1

jit:
Failed running call_function <built-in function avg_pool2d>(*(FakeTensor(..., size=(5, 24, 4, 16)), (3, 3), (3, 3), 2, False, True, None), **{}):
pad should be at most half of effective kernel size, but got pad=2, kernel_size=3 and dilation=1

from user code:
   File "<string>", line 22, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/pooling.py", line 756, in forward
    return F.avg_pool2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''