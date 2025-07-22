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



class ModuleTest(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv3d(in_channels=1, out_channels=2, stride=(1, 1), kernel_size=2)
        self.relu1 = torch.nn.ReLU6(inplace=False)

    def forward(self, x):
        conv1 = self.conv1(x)
        relu1 = self.relu1(conv1)
        return relu1




func = ModuleTest().to('cuda')



x = torch.randn(1, 1, 5, 5, 5)


test_inputs = [x]

# JIT_FAIL
'''
direct:
expected stride to be a single integer value or a list of 3 values to match the convolution dimensions, but got stride=[1, 1]

jit:
Failed running call_module L__self___conv1(*(FakeTensor(..., device='cuda:0', size=(1, 1, 5, 5, 5)),), **{}):
expected stride to be a single integer value or a list of 3 values to match the convolution dimensions, but got stride=[1, 1]

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''