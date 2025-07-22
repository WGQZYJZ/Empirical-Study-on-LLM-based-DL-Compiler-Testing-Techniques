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
        self.conv2 = torch.nn.Conv2d(3, 3, 2)
        self.conv3 = torch.nn.Conv2d(3, 3, 1)
        self.bn = torch.nn.BatchNorm2d(3)

    def forward(self, x2, x3):
        s = self.conv1(x2)
        t = self.conv2(x3)
        u = self.conv3((s + t))
        y = self.bn(u)
        return (s, u, y)




func = Model().to('cuda')



x2 = torch.randn(16, 3, 6, 6)



x3 = torch.randn(1, 3, 6, 6)


test_inputs = [x2, x3]

# JIT_FAIL
'''
direct:
The size of tensor a (4) must match the size of tensor b (5) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(16, 3, 4, 4)), FakeTensor(..., device='cuda:0', size=(1, 3, 5, 5))), **{}):
Attempting to broadcast a dimension of length 5 at -1! Mismatching argument at index 1 had torch.Size([1, 3, 5, 5]); but expected shape should be broadcastable to [16, 3, 4, 4]

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''