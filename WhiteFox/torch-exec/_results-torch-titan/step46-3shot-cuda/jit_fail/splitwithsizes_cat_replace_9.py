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
        super(Model, self).__init__()
        self.conv0 = torch.nn.Conv2d(3, 64, 3, stride=1, padding=1)
        self.conv1 = torch.nn.Conv2d(3, 64, 1, stride=2, padding=0, bias=False)
        self.conv2 = torch.nn.Conv2d(64, 64, 3, stride=1, padding=1, bias=False)
        self.conv3 = torch.nn.Conv2d(64, 64, 1, stride=1, padding=0, bias=False)

    def forward(self, v1):
        split_tensors = torch.split(self.conv0(v1), [1, 1, 1, 1, 1, 1, 1], dim=1)
        concatenated_tensor = torch.cat(split_tensors, dim=1)
        split_tensors = torch.split(concatenated_tensor, [1, 1, 1, 1, 1, 1], dim=1)
        concatenated_tensor = torch.cat(split_tensors, dim=1)
        split_tensors = torch.split(concatenated_tensor, [1, 1, 1, 1, 1, 1], dim=1)
        concatenated_tensor = torch.cat(split_tensors, dim=1)
        split_tensors = torch.split(concatenated_tensor, [1, 1, 1, 1], dim=1)
        concatenated_tensor = torch.cat(split_tensors, dim=1)
        return (concatenated_tensor, torch.split(self.conv1(v1), [1, 1, 1, 1, 1, 1, 1], dim=1), torch.split(self.conv2(v1), [1, 1, 1, 1, 1, 1], dim=1), torch.split(self.conv3(v1), [1, 1, 1, 1], dim=1))




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
split_with_sizes expects split_sizes to sum exactly to 64 (input tensor's size at dimension 1), but got split_sizes=[1, 1, 1, 1, 1, 1, 1]

jit:
Failed running call_function <function split at 0x728c918ee0d0>(*(FakeTensor(..., device='cuda:0', size=(1, 64, 64, 64)), [1, 1, 1, 1, 1, 1, 1]), **{'dim': 1}):
Split sizes don't add up to the tensor's size in the given dimension

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''