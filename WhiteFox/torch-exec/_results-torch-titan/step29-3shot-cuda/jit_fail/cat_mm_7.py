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
        self.conv1 = torch.nn.Conv2d(2, 10, (10, 15))
        self.gelu_act = torch.nn.GELU()
        self.conv2 = torch.nn.Conv1d(20, 10, 10)
        self.softmax = torch.nn.Softmax(1)

    def forward(self, x):
        v1 = self.conv1(x).permute(0, 2, 3, 1)
        v2 = self.conv1(x).permute(0, 2, 3, 1)
        v3 = self.conv1(x).permute(0, 2, 3, 1)
        res = torch.cat([v1, v2, v3], 2).permute(0, 3, 1, 2)
        res = self.gelu_act(res)
        res = self.conv2(res).permute(0, 2, 1)
        return self.softmax(res)




func = Model().to('cuda')



x = torch.randn(1, 2, 10, 15)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Expected 2D (unbatched) or 3D (batched) input to conv1d, but got input of size: [1, 10, 1, 3]

jit:
Failed running call_module L__self___conv2(*(FakeTensor(..., device='cuda:0', size=(1, 10, 1, 3)),), **{}):
Expected 2D (unbatched) or 3D (batched) input to conv1d, but got input of size: [1, 10, 1, 3]

from user code:
   File "<string>", line 30, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''