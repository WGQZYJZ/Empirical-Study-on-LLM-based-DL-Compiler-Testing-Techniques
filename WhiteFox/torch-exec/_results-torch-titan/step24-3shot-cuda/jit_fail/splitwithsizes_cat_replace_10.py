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
        self.features = torch.nn.Sequential(torch.nn.Conv2d(3, 32, 3, 1, 1), torch.nn.ReLU(inplace=False), torch.nn.Conv2d(32, 32, 3, 1, 1))
        self.concat = torch.nn.Sequential(torch.nn.Conv2d(32, 32, 3, 1, 0))
        self.features_1 = torch.nn.Sequential(torch.nn.Conv2d(32, 32, 3, 1, 2))
        self.features_2 = torch.nn.Sequential(torch.nn.Conv2d(32, 32, 1, 2), torch.nn.ReLU(inplace=True))

    def forward(self, v1):
        split_tensors = torch.split(v1, [1, 1, 1], dim=1)
        concatenated_tensor = torch.cat(split_tensors, dim=1)
        (intermediate, _) = self.features_1(split_tensors[1])
        (intermediate, _) = self.features_2(intermediate)
        (_, split) = self.features(split_tensors[1])
        return (concatenated_tensor, torch.split(v1, [1, 1, 1], dim=1), intermediate, split)




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [32, 32, 3, 3], expected input[1, 1, 64, 64] to have 32 channels, but got 1 channels instead

jit:
Failed running call_module L__self___features_1_0(*(FakeTensor(..., device='cuda:0', size=(1, 1, 64, 64)),), **{}):
Given groups=1, weight of size [32, 32, 3, 3], expected input[1, 1, 64, 64] to have 32 channels, but got 1 channels instead

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''