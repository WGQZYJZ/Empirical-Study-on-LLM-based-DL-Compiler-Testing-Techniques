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
        block_0 = [torch.nn.BatchNorm2d(32)]
        block_1 = [torch.nn.ReLU()]
        block_2 = [torch.nn.Conv2d(32, 64, 3, 1, 0, bias=False), torch.nn.BatchNorm2d(64)]
        block_3 = [torch.nn.ReLU()]
        block_4 = [torch.nn.Conv2d(64, 128, 1, 1, 0, bias=False), torch.nn.BatchNorm2d(128)]
        self.features = torch.nn.Sequential(*block_0, *block_1, *block_2, *block_3, *block_4)

    def forward(self, v1):
        split_tensors = torch.split(v1, [128, 128, 128, 128], dim=1)
        concatenated_tensor = torch.cat(split_tensors, dim=1)
        return (concatenated_tensor, torch.split(v1, [128, 128, 128, 128], dim=1))




func = Model().to('cuda')



x1 = torch.randn(1, 3, 128, 128)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
split_with_sizes expects split_sizes to sum exactly to 3 (input tensor's size at dimension 1), but got split_sizes=[128, 128, 128, 128]

jit:
Failed running call_function <function split at 0x713c3b86f0d0>(*(FakeTensor(..., device='cuda:0', size=(1, 3, 128, 128)), [128, 128, 128, 128]), **{'dim': 1}):
Split sizes don't add up to the tensor's size in the given dimension

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''