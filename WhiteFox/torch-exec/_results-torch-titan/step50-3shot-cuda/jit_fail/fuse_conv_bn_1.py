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
        self.conv1 = torch.nn.Conv2d(3, 3, 3)
        self.conv2 = torch.nn.Conv2d(3, 3, 3)
        self.pooling = torch.nn.MaxPool2d(3)
        self.bn = torch.nn.BatchNorm2d(3)

    def forward(self, x1):
        s = self.conv1(x1)
        t = self.conv2(s)
        w = self.pooling(s)
        y = self.bn(s)
        z = self.bn(w)
        return (y + z)




func = Model().to('cuda')



x = torch.randn(1, 3, 224, 224)


test_inputs = [x]

# JIT_FAIL
'''
direct:
The size of tensor a (222) must match the size of tensor b (74) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 3, 222, 222)), FakeTensor(..., device='cuda:0', size=(1, 3, 74, 74))), **{}):
Attempting to broadcast a dimension of length 74 at -1! Mismatching argument at index 1 had torch.Size([1, 3, 74, 74]); but expected shape should be broadcastable to [1, 3, 222, 222]

from user code:
   File "<string>", line 30, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''