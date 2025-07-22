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
        self.features = torch.nn.Sequential(torch.nn.ConvTranspose2d(1, 32, (3, 3), stride=2), torch.nn.Conv2d(32, 64, (3, 3), stride=2), torch.nn.ReLU())
        self.fc = torch.nn.Linear(50176, 10)

    def forward(self, x):
        x = self.features(x)
        x = torch.flatten(x, 1)
        x = self.fc(x)
        output = torch.nn.functional.relu(x)
        return x




func = Model().to('cuda')



x1 = torch.randn(1, 3, 32, 32)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [1, 32, 3, 3], expected input[1, 3, 32, 32] to have 1 channels, but got 3 channels instead

jit:
Failed running call_module L__self___features_0(*(FakeTensor(..., device='cuda:0', size=(1, 3, 32, 32)),), **{}):
Given transposed=1, weight of size [1, 32, 3, 3], expected input[1, 3, 32, 32] to have 1 channels, but got 3 channels instead

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''