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
        self.conv_transpose = torch.nn.ConvTranspose2d(9, 6, kernel_size=(48, 17), stride=(1, 1), bias=False)
        self.batch_norm = torch.nn.BatchNorm2d(6)

    def forward(self, x1):
        v1 = torch.squeeze(x1, dim=0)
        v2 = self.conv_transpose(v1)
        v3 = torch.tanh(v2)
        v4 = self.batch_norm(v3)
        v5 = v4.unsqueeze(0)
        return v5



func = Model().to('cpu')



x1 = torch.zeros(1, 1, 9, 9, dtype=torch.float32)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [9, 6, 48, 17], expected input[1, 1, 9, 9] to have 9 channels, but got 1 channels instead

jit:
Failed running call_function <built-in method conv_transpose2d of type object at 0x7d4fbfd96ec0>(*(FakeTensor(..., size=(1, 9, 9)), Parameter(FakeTensor(..., size=(9, 6, 48, 17), requires_grad=True)), None, (1, 1), (0, 0), (0, 0), 1, (1, 1)), **{}):
Given transposed=1, weight of size [9, 6, 48, 17], expected input[1, 1, 9, 9] to have 9 channels, but got 1 channels instead

from user code:
   File "<string>", line 22, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 1162, in forward
    return F.conv_transpose2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''