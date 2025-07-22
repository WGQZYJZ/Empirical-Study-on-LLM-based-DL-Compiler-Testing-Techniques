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



class ModelTanh(torch.nn.Module):

    def __init__(self):
        super(ModelTanh, self).__init__()
        self.conv1 = torch.nn.Conv2d(1, 3, kernel_size=(192, 29, 4), stride=(192, 29, 4), groups=1)
        self.conv2 = torch.nn.Conv2d(3, 3, kernel_size=(325, 6, 34), stride=(325, 6, 34), groups=1, dilation=253)

    def forward(self, x1):
        x2 = self.conv1(x1)
        x3 = self.conv2(x2)
        x4 = torch.tanh(x3)
        return x4




func = ModelTanh().to('cuda')



x1 = torch.randn(1, 1, 352, 946)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
expected padding to be a single integer value or a list of 3 values to match the convolution dimensions, but got padding=[0, 0]

jit:
Failed running call_module L__self___conv1(*(FakeTensor(..., device='cuda:0', size=(1, 1, 352, 946)),), **{}):
expected padding to be a single integer value or a list of 3 values to match the convolution dimensions, but got padding=[0, 0]

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''