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
        super(Model, self).__init__()
        self.conv = nn.Conv2d(3, 32, 3, 1)
        self.bn = nn.BatchNorm2d(32)
        self.fc1 = nn.Linear(6272, 1024)
        self.fc2 = nn.Linear(1024, 17)

    def forward(self, x):
        x = self.conv(x)
        x = self.bn(x)
        x = x.view(x.len(0), (- 1))
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x




func = Model().to('cuda')



x = torch.randn(10, 3, 224, 224)


test_inputs = [x]

# JIT_FAIL
'''
direct:
'Tensor' object has no attribute 'len'

jit:
Failed running call_method len(*(FakeTensor(..., device='cuda:0', size=(10, 32, 222, 222)), 0), **{}):
'FakeTensor' object has no attribute 'len'

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''