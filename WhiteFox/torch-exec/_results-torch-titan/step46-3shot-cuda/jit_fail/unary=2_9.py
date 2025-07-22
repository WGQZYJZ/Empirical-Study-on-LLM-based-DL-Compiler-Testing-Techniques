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
        self.conv_transpose1 = torch.nn.ConvTranspose2d(1, 1, 1, stride=(1, 1), padding=(0, 0))
        self.conv_transpose2 = torch.nn.ConvTranspose2d(2, 1, 3, stride=(2, 2), padding=(0, 0))
        self.conv_transpose3 = torch.nn.ConvTranspose2d(1, 2, 2, stride=(1, 3), padding=(1, 2))
        self.conv2d = torch.nn.Conv2d(1, 1, 1, stride=1, padding=0)
        self.conv1d = torch.nn.Conv1d(1, 1, 1, stride=1, padding=0)

    def forward(self, x1):
        v2 = self.conv_transpose1(x1)
        v1 = self.conv_transpose2(v2)
        v4 = self.conv_transpose3(v1)
        v3 = self.conv2d(v4)
        v5 = self.conv1d(v3)
        return v5




func = Model().to('cuda')



x1 = torch.randn(1, 1, 3, 3)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [2, 1, 3, 3], expected input[1, 1, 3, 3] to have 2 channels, but got 1 channels instead

jit:
Failed running call_module L__self___conv_transpose2(*(FakeTensor(..., device='cuda:0', size=(1, 1, 3, 3)),), **{}):
Given transposed=1, weight of size [2, 1, 3, 3], expected input[1, 1, 3, 3] to have 2 channels, but got 1 channels instead

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''