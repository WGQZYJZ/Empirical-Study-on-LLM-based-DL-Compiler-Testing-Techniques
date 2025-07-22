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



class Model(nn.Module):

    def __init__(self):
        super().__init__()
        self.fc_1 = nn.Linear(3, 3)
        self.maxpool = nn.MaxPool2d(4, stride=4)
        self.fc_2 = nn.Linear(3, 1)

    def forward(self, x):
        x = self.fc_1(x)
        x = self.maxpool(x)
        x = self.fc_2(x)
        x = F.flatten(x)
        return x




func = Model().to('cuda')



x1 = torch.randn(1, 3)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
non-empty 3D or 4D (batch mode) tensor expected for input

jit:
Failed running call_module L__self___maxpool(*(FakeTensor(..., device='cuda:0', size=(1, 3)),), **{}):
Dimension out of range (expected to be in range of [-2, 1], but got -3)

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''