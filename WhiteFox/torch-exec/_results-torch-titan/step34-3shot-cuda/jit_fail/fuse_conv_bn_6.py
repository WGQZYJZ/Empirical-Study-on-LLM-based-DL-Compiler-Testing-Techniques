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
        self.conv1 = torch.nn.Conv1d(4, 4, 5)
        self.batchnorm1d = torch.nn.BatchNorm1d(4)
        self.relu1 = torch.nn.ReLU()
        self.relu2 = torch.nn.ReLU()
        self.con2 = torch.nn.Conv2d(4, 3, 5)

    def forward(self, x1):
        s = self.conv1(x1)
        t = s.transpose(1, 2)
        r1 = self.relu1(s)
        bn1 = self.batchnorm1d(s)
        y = (r1 + bn1)
        r2 = self.relu2(y)
        z = self.con2(r2.unsqueeze(0).unsqueeze(0))
        return z.squeeze(0).squeeze(0)




func = Model().to('cuda')



x1 = torch.randn(1, 4, 20)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected 3D (unbatched) or 4D (batched) input to conv2d, but got input of size: [1, 1, 1, 4, 16]

jit:
Failed running call_module L__self___con2(*(FakeTensor(..., device='cuda:0', size=(1, 1, 1, 4, 16)),), **{}):
Expected 3D (unbatched) or 4D (batched) input to conv2d, but got input of size: [1, 1, 1, 4, 16]

from user code:
   File "<string>", line 32, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''