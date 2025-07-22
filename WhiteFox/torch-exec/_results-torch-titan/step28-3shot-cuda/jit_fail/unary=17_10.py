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
        self.conv1 = torch.nn.ConvTranspose2d(3, 5, 3, padding=(1, 1, 1, 1), stride=(1, 1))
        self.conv2 = torch.nn.ConvTranspose2d(5, 5, 3, padding=(1, 1, 1, 1), stride=(1, 1))
        self.conv3 = torch.nn.ConvTranspose2d(5, 3, 3, padding=(1, 1, 1, 1), stride=(1, 1))

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = torch.relu(v1)
        v3 = self.conv2(v2)
        v4 = torch.relu(v3)
        v5 = self.conv3(v4)
        v6 = torch.relu(v5)
        return v5




func = Model().to('cuda')



x1 = torch.randn(1, 3, 128, 128)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
expected padding to be a single integer value or a list of 2 values to match the convolution dimensions, but got padding=[1, 1, 1, 1]

jit:
Failed running call_module L__self___conv1(*(FakeTensor(..., device='cuda:0', size=(1, 3, 128, 128)),), **{}):
expected padding to be a single integer value or a list of 2 values to match the convolution dimensions, but got padding=[1, 1, 1, 1]

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''