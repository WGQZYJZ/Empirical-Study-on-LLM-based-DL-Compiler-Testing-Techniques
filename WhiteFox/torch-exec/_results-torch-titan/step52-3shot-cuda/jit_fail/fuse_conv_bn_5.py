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
        self.conv_1 = torch.nn.Conv2d(512, 512, (3, 3), stride=(2, 2), padding=(1, 1), bias=False)
        self.bn_1 = torch.nn.BatchNorm2d(512, track_running_stats=True)
        self.conv_2 = torch.nn.Conv2d(512, 256, (1, 1), stride=(1, 1), bias=False)
        self.bn_2 = torch.nn.BatchNorm2d(256, track_running_stats=True)

    def forward(self, x3):
        x = self.conv_1(x3)
        x = self.bn_1(x)
        x = self.conv_2(x)
        x = self.bn_2(x)
        return ((x3 + x) + x)




func = Model().to('cuda')



x3 = torch.randn(1, 512, 8, 8)


test_inputs = [x3]

# JIT_FAIL
'''
direct:
The size of tensor a (8) must match the size of tensor b (4) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 512, 8, 8)), FakeTensor(..., device='cuda:0', size=(1, 256, 4, 4))), **{}):
Attempting to broadcast a dimension of length 4 at -1! Mismatching argument at index 1 had torch.Size([1, 256, 4, 4]); but expected shape should be broadcastable to [1, 512, 8, 8]

from user code:
   File "<string>", line 29, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''