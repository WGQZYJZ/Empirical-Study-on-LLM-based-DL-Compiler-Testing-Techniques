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
        torch.manual_seed(0)
        super().__init__()
        self.conv = torch.nn.Conv1d(15, 1, 3, 1, 1, bias=False)
        self.bn = torch.nn.BatchNorm1d(1, track_running_stats=False)
        torch.manual_seed(0)
        self.fc = torch.nn.Linear(10, 20, bias=False)

    def forward(self, input):
        x = self.conv(input)
        x = self.bn(x)
        features = x.permute(0, 2, 1).contiguous().view((- 1), 10)
        return torch.sigmoid(self.fc(features))




func = Model().to('cuda')



input = torch.randn(1, 15, 6)


test_inputs = [input]

# JIT_FAIL
'''
direct:
shape '[-1, 10]' is invalid for input of size 6

jit:
Failed running call_method view(*(FakeTensor(..., device='cuda:0', size=(1, 6, 1)), -1, 10), **{}):
shape '[-1, 10]' is invalid for input of size 6

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''