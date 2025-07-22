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
        self.conv1 = torch.nn.Conv1d(1, 2, 1)
        self.conv2 = torch.nn.Conv1d(2, 2, 1)
        self.conv3 = torch.nn.Conv1d(2, 2, 1)
        self.conv4 = torch.nn.Conv1d(2, 2, 1)
        self.conv5 = torch.nn.Conv1d(2, 2, 1)
        self.conv6 = torch.nn.Conv1d(2, 2, 1)
        self.conv7 = torch.nn.Conv1d(2, 2, 1)

    def forward(self, input):
        x = torch.nn.functional.relu(self.conv1(input))
        out = self.conv6(torch.nn.functional.relu(self.conv2(x)))
        out = self.conv3(torch.nn.functional.relu(self.conv4(out)))
        out = self.conv5(torch.nn.functional.relu(self.conv7(out)))
        x = self.conv2(torch.nn.functional.relu(self.conv1(input)))
        x = self.conv7(torch.nn.functional.relu(self.conv6(x)))
        x = self.conv4(torch.nn.functional.relu(self.conv1(x)))
        out = self.conv3(torch.nn.functional.relu(self.conv5(out)))
        return out




func = Model().to('cuda')



input = torch.randn(3, 1, 20)


test_inputs = [input]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [2, 1, 1], expected input[3, 2, 20] to have 1 channels, but got 2 channels instead

jit:
Failed running call_module L__self___conv1(*(FakeTensor(..., device='cuda:0', size=(3, 2, 20)),), **{}):
Invalid channel dimensions

from user code:
   File "<string>", line 34, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''