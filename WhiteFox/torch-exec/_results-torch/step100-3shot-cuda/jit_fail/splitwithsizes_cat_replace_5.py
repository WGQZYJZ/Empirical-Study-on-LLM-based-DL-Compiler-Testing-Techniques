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

class Block(torch.nn.Module):

    def __init__(self, num_output_channels, stride):
        super(Block, self).__init__()
        self.conv1 = torch.nn.Conv2d(128, num_output_channels, 3, stride, padding=1)
        self.relu = torch.nn.ReLU(inplace=True)

    def forward(self, x1):
        split_tensors = torch.split(x1, [1, 1, 1, 1, 1, 1], dim=1)
        concatenated_tensor = torch.cat(split_tensors, dim=1)
        return self.relu(self.conv1(concatenated_tensor))

class Model(torch.nn.Module):

    def __init__(self):
        super(Model, self).__init__()
        self.conv1 = torch.nn.Conv2d(3, 128, 3, 1, padding=1)
        self.block = Block(128, 1)
        self.conv2 = torch.nn.Conv2d(128, 3, 3, 1, padding=1)

    def forward(self, x1):
        split_tensors = torch.split(x1, [1, 1, 1], dim=1)
        concatenated_tensor = torch.cat(split_tensors, dim=1)
        return (concatenated_tensor, self.conv2(self.block(self.conv1(concatenated_tensor))))



func = Model().to('cuda')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
split_with_sizes expects split_sizes to sum exactly to 128 (input tensor's size at dimension 1), but got split_sizes=[1, 1, 1, 1, 1, 1]

jit:
Failed running call_function <function split at 0x716dfd1bbf70>(*(FakeTensor(..., device='cuda:0', size=(1, 128, 64, 64)), [1, 1, 1, 1, 1, 1]), **{'dim': 1}):
Split sizes add up to 6 but got the tensor's size of 128

from user code:
   File "<string>", line 36, in forward
  File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''