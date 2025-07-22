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
        super().__init__()
        kernel_size = 9616
        input_dim = 3
        output_dim = 97
        stride = 4
        padding = 142
        self.conv = torch.nn.Conv1d(input_dim, output_dim, kernel_size, stride=stride, padding=padding)

    def forward(self, x):
        y1 = self.conv(x)
        y2 = torch.tanh(y1)
        return y2




func = ModelTanh().to('cuda')



x = torch.randn(20, 3, 2570)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (2854). Kernel size: (9616). Kernel size can't be greater than actual input size

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(20, 3, 2570)),), **{}):
Trying to create tensor with negative dimension -1690: [20, 97, -1690]

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''