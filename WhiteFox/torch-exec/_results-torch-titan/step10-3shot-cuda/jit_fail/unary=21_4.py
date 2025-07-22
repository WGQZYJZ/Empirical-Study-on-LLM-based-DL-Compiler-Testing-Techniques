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
        self.conv1 = torch.nn.Conv2d(3, 3, kernel_size=3, padding=2)

    def forward(self, x):
        x1 = self.conv1(x)
        x1 = torch.cat([x, x1], axis=1)
        x2 = torch.tanh(x1)
        x2 = torch.cat([x1, x2], axis=1)
        return x2




func = ModelTanh().to('cuda')



x = torch.randn(1, 3, 35, 35)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Sizes of tensors must match except in dimension 1. Expected size 35 but got size 37 for tensor number 1 in the list.

jit:
Failed running call_function <built-in method cat of type object at 0x7e160b0699e0>(*([FakeTensor(..., device='cuda:0', size=(1, 3, 35, 35)), FakeTensor(..., device='cuda:0', size=(1, 3, 37, 37))],), **{'axis': 1}):
Sizes of tensors must match except in dimension 1. Expected 35 but got 37 for tensor number 1 in the list

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''