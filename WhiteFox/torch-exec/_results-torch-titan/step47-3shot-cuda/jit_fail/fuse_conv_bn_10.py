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
        self.conv = torch.nn.Conv2d(4, 4, 2)
        self.conv1 = torch.nn.Conv2d(4, 4, 2)
        self.conv2 = torch.nn.ConvTranspose2d(4, 4, 2)
        self.fc = torch.nn.Linear(4, 1)

    def forward(self, x):
        x = self.conv(x)
        z = self.conv1(x)
        z = torch.mean(z, dim=1, keepdim=True)
        x = torch.transpose(x, 1, 2)
        x = self.conv2(x, output_size=(z, x.shape[2]))
        x = torch.transpose(x, 1, 2)
        return x




func = Model().to('cuda')



x = torch.randn(1, 1, 8, 8)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [4, 4, 2, 2], expected input[1, 1, 8, 8] to have 4 channels, but got 1 channels instead

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(1, 1, 8, 8)),), **{}):
Given groups=1, weight of size [4, 4, 2, 2], expected input[1, 1, 8, 8] to have 4 channels, but got 1 channels instead

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''