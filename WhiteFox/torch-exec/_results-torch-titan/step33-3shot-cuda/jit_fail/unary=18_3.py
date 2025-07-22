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
        self.conv1 = torch.nn.Conv2d(in_channels=1, out_channels=32, kernel_size=3, stride=2, padding=2)
        self.conv2 = torch.nn.Conv2d(in_channels=32, out_channels=16, kernel_size=3, stride=2, padding=2)
        self.conv3 = torch.nn.Conv2d(in_channels=16, out_channels=16, kernel_size=3, stride=2, padding=2)
        self.conv4 = nn.Conv2d(in_channels=16, out_channels=16, kernel_size=3, stride=2, padding=2)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = nn.Sigmoid()(v1)
        v3 = self.conv2(v2)
        v4 = torch.Sigmoid()(v3)
        v5 = self.conv2(v4)
        v6 = nn.Sigmoid()(v5)
        v7 = self.conv3(v6)
        v8 = torch.tanh(v7)
        v9 = self.conv4(v8)
        v10 = nn.Sigmoid()(v9)
        return v10




func = Model().to('cuda')



x1 = torch.randn(1, 1, 224, 224)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
module 'torch' has no attribute 'Sigmoid'

jit:
module 'torch' has no attribute 'Sigmoid'

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''