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
        self.conv = torch.nn.Conv2d(2, 6, 1, stride=1, padding=1)

    def forward(self, x1, other=None, padding1=None, padding2=None):
        v1 = self.conv(x1)
        if (other == None):
            other = torch.randn(v1.shape)
            if (padding1 == None):
                padding1 = torch.randn(v1.shape)
                if (v1.shape[0] == 3):
                    if (v1.shape[1] == 2):
                        v1 = torch.randn(v1.shape)
                        if (self.conv.out_channels == 5):
                            if (v1.shape[0] == 6):
                                if (v1.shape[1] == 1):
                                    padding2 = torch.randn(v1.shape)
                    elif (self.conv.out_channels > 9):
                        if (v1.shape[0] == 2):
                            v1 = torch.randn(v1.shape)
            elif (v1.shape[0] == 3):
                v1 = torch.rand(v1.shape)
                if (padding2 == None):
                    padding2 = torch.randn(v1.shape)
                    if (self.conv.in_channels == 5):
                        if (v1.shape[0] == 3):
                            if (padding1.shape[0] == 3):
                                padding1 = torch.randn(v1.shape)
                                if (padding2.shape[0] == 3):
                                    if (v1.shape[0] == other.shape[0]):
                                        if (padding1.shape[1] == 2):
                                            if (padding1.shape[1] == other.shape[0]):
                                                if (padding2.shape[0] == other.shape[0]):
                                                    if (padding1.shape[0] == padding2.shape[0]):
                                                        other = torch.randn(v1.shape)
                elif (padding2.shape[0] == 3):
                    padding2 = torch.randn(v1.shape)
            else:
                v1 = torch.randn(v1.shape)
        elif (other.shape[0] == 6):
            other = torch.randn(v1.shape)
        v2 = (v1 + other)
        return v2




func = Model().to('cuda')



x1 = torch.randn(1, 2, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu!

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 6, 66, 66)), FakeTensor(..., size=(1, 6, 66, 66))), **{}):
Unhandled FakeTensor Device Propagation for aten.add.Tensor, found two different devices cuda:0, cpu

from user code:
   File "<string>", line 58, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''