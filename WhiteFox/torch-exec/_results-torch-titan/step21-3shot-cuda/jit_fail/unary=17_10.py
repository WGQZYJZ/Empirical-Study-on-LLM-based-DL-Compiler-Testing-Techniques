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
        self.conv = torch.nn.ConvTranspose2d(2, 4, (2, 3), stride=(2, 1), padding=(21, 17))
        self.conv1 = torch.nn.ConvTranspose2d(3, 2, 1, stride=1, padding=0)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.relu(v1)
        v3 = self.conv1(v2)
        return v3




func = Model().to('cuda')



x1 = torch.randn(1, 2, 224, 224)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [3, 2, 1, 1], expected input[1, 4, 406, 192] to have 3 channels, but got 4 channels instead

jit:
Failed running call_module L__self___conv1(*(FakeTensor(..., device='cuda:0', size=(1, 4, 406, 192)),), **{}):
Given transposed=1, weight of size [3, 2, 1, 1], expected input[1, 4, 406, 192] to have 3 channels, but got 4 channels instead

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''