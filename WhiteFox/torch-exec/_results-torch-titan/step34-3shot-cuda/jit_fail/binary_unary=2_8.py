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
        self.conv1 = torch.nn.Conv2d(3, 16, (11, 11), stride=(1, 1), padding=(5, 5))
        self.conv2 = torch.nn.Conv2d(16, 32, (3, 3), stride=(2, 2), padding=(1, 1))
        self.conv3 = torch.nn.Conv2d(32, 48, (1, 1), stride=(1, 1), padding=(0, 0))
        self.conv4 = torch.nn.Conv2d(1, 3, (5, 5), stride=(1, 1), padding=(2, 2))

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = (v1 - 0.5)
        v3 = F.relu(v2)
        v4 = torch.squeeze(v3, 0)
        v5 = self.conv2(v4)
        v7 = (v5 - 0.1)
        v6 = F.relu(v7)
        v8 = self.conv3(v6)
        v10 = (v8 - 0.1)
        v9 = F.relu(v10)
        v11 = torch.squeeze(v9, 0)
        v13 = self.conv4(v11)
        v15 = (v13 - 0.1)
        v16 = F.relu(v15)
        return v16




func = Model().to('cuda')



x1 = torch.randn(1, 3, 23, 23)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [3, 1, 5, 5], expected input[1, 48, 12, 12] to have 1 channels, but got 48 channels instead

jit:
Failed running call_module L__self___conv4(*(FakeTensor(..., device='cuda:0', size=(48, 12, 12)),), **{}):
Given groups=1, weight of size [3, 1, 5, 5], expected input[1, 48, 12, 12] to have 1 channels, but got 48 channels instead

from user code:
   File "<string>", line 36, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''