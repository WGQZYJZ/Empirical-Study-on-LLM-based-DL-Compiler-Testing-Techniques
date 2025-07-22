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
        self.conv1 = torch.nn.ConvTranspose2d(1, 32, 3, stride=1)
        self.conv2 = torch.nn.ConvTranspose2d(32, 16, 3, stride=2, padding=1)
        self.conv3 = torch.nn.ConvTranspose2d(16, 8, 3, stride=1, padding=1)
        self.conv4 = torch.nn.ConvTranspose2d(8, 4, 3, stride=1, padding=1)
        self.conv5 = torch.nn.ConvTranspose2d(4, 2, 3, stride=1, padding=1)
        self.convfinal = torch.nn.ConvTranspose2d(2, 4, 3, stride=1, padding=2)

    def forward(self, x, x_len):
        x_len = x_len.reshape(1, (- 1), 1).float()
        x = torch.mul(x, x_len)
        x1 = F.relu(self.conv1(x))
        x2 = F.relu(self.conv2(x1))
        x3 = F.relu(self.conv3(x2))
        x4 = F.relu(self.conv4(x3))
        x5 = F.relu(self.conv5(x4))
        xn = torch.sigmoid(self.convfinal(x5))
        xn = torch.mul(xn, x_len)
        return xn




func = Model().to('cuda')



x = torch.randn(2, 2, 10, 10)



x_len = torch.randn(2)


test_inputs = [x, x_len]

# JIT_FAIL
'''
direct:
The size of tensor a (10) must match the size of tensor b (2) at non-singleton dimension 2

jit:
Failed running call_function <built-in method mul of type object at 0x7658ab2699e0>(*(FakeTensor(..., device='cuda:0', size=(2, 2, 10, 10)), FakeTensor(..., device='cuda:0', size=(1, 2, 1))), **{}):
Attempting to broadcast a dimension of length 2 at -2! Mismatching argument at index 1 had torch.Size([1, 2, 1]); but expected shape should be broadcastable to [2, 2, 10, 10]

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''