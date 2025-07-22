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
        self.convtranspose1 = torch.nn.ConvTranspose1d(64, 512, kernel_size=3, stride=1, padding=1)
        self.convtranspose2 = torch.nn.ConvTranspose2d(64, 512, 3, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.convtranspose1(x1)
        v2 = self.convtranspose2(x1)
        v3 = torch.mean(torch.reshape(v1, ((- 1), 512, 1)))
        v4 = torch.sigmoid(v3)
        return (v4 + v2)




func = Model().to('cuda')



x1 = torch.randn(1, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [64, 512, 3, 3], expected input[1, 1, 64, 64] to have 64 channels, but got 1 channels instead

jit:
Failed running call_module L__self___convtranspose2(*(FakeTensor(..., device='cuda:0', size=(1, 64, 64)),), **{}):
Given transposed=1, weight of size [64, 512, 3, 3], expected input[1, 1, 64, 64] to have 64 channels, but got 1 channels instead

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''