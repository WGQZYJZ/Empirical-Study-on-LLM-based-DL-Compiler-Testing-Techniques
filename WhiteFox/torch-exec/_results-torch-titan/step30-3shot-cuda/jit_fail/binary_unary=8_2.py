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
        self.conv1 = torch.nn.Conv2d(3, 8, 3, stride=1, padding=1, dilation=2)
        self.conv2 = torch.nn.Conv2d(3, 8, 3, stride=1, padding=1, dilation=0)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(x1)
        v3 = (v1 + v2)
        v4 = torch.relu(v3)
        return v4




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
CUDNN_BACKEND_CONVOLUTION_DESCRIPTOR: cudnnFinalize Failed cudnn_status: CUDNN_STATUS_BAD_PARAM

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 8, 62, 62)), FakeTensor(..., device='cuda:0', size=(1, 8, 66, 66))), **{}):
Attempting to broadcast a dimension of length 66 at -1! Mismatching argument at index 1 had torch.Size([1, 8, 66, 66]); but expected shape should be broadcastable to [1, 8, 62, 62]

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''