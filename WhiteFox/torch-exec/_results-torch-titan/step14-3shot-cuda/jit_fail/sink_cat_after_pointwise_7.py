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
        self.features = torch.nn.Sequential(*[torch.nn.Conv2d(3, 10, kernel_size=5), torch.nn.ReLU(), torch.nn.MaxPool2d(kernel_size=2, stride=2, return_indices=(not bool())), torch.nn.Conv2d(10, 20, kernel_size=5), torch.nn.ReLU(), torch.nn.MaxPool2d(kernel_size=2, stride=2, return_indices=(not bool())), torch.nn.ReLU()]).eval()

    def forward(self, x):
        t1 = torch.cat([x, x], dim=1)
        t2 = t1.tanh()
        t3 = self.features(t2)
        y = t3
        return y




func = Model().to('cuda')



x = torch.randn(2, 3, 10, 10)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [10, 3, 5, 5], expected input[2, 6, 10, 10] to have 3 channels, but got 6 channels instead

jit:
Failed running call_module L__self___features_0(*(FakeTensor(..., device='cuda:0', size=(2, 6, 10, 10)),), **{}):
Given groups=1, weight of size [10, 3, 5, 5], expected input[2, 6, 10, 10] to have 3 channels, but got 6 channels instead

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''