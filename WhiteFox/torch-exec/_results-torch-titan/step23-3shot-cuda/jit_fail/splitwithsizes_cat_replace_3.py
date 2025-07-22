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
        self.features = torch.nn.Sequential(torch.nn.ReLU(inplace=True), torch.nn.MaxPool2d(3, 2, 0), torch.nn.Sequential(torch.nn.Dropout2d(p=0.5, inplace=True), torch.nn.ConstantPad2d((1, 1, 1, 1), value=0), torch.nn.Conv2d(64, 40, 3, 1, 0)), torch.nn.MaxPool2d(3, 2, 1), torch.nn.ReLU(inplace=True), torch.nn.ConvTranspose2d(40, 64, 3, 2, 0))
        self.conv2 = torch.nn.ConvTranspose2d(64, 80, 4, 2, 1)
        self.conv3 = torch.nn.ConvTranspose2d(64, 80, 3, 1, 0)

    def forward(self, v1, v2):
        split_tensors = torch.split(v1, [1, 1, 1], dim=1)
        concatenated_tensor = torch.cat(split_tensors, dim=1)
        return (torch.cat([self.conv2(concatenated_tensor), self.conv3(v2)], dim=1), torch.split(v1, [1, 1, 1], dim=1))




func = Model().to('cuda')



x1 = torch.randn(1, 64, 64, 64)



x2 = torch.randn(1, 64, 64, 64)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
split_with_sizes expects split_sizes to sum exactly to 64 (input tensor's size at dimension 1), but got split_sizes=[1, 1, 1]

jit:
Failed running call_function <function split at 0x7e713a4ad0d0>(*(FakeTensor(..., device='cuda:0', size=(1, 64, 64, 64)), [1, 1, 1]), **{'dim': 1}):
Split sizes don't add up to the tensor's size in the given dimension

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''