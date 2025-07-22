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
        self.conv1 = torch.nn.Conv2d(3, 1, 2, stride=4, padding=2)
        self.conv2 = torch.nn.Conv2d(3, 1, 1, stride=2, padding=2)
        self.conv3 = torch.nn.Conv2d(3, 1, 1, stride=2, padding=2)
        self.conv4 = torch.nn.Conv2d(3, 1, 1, stride=2, padding=2)

    def forward(self, x):
        v1 = self.conv1(x)
        v2 = ((self.conv2(x) - self.conv3(x)) + self.conv4(x))
        return (v1 + v2)




func = Model().to('cuda')



x1 = torch.randn(1, 3, 17, 17)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (5) must match the size of tensor b (11) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 1, 5, 5)), FakeTensor(..., device='cuda:0', size=(1, 1, 11, 11))), **{}):
Attempting to broadcast a dimension of length 11 at -1! Mismatching argument at index 1 had torch.Size([1, 1, 11, 11]); but expected shape should be broadcastable to [1, 1, 5, 5]

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''