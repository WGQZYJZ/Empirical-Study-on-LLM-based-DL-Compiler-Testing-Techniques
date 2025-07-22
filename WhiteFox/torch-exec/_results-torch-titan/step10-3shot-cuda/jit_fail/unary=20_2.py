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
        self.trconv = torch.nn.ConvTranspose2d(in_channels=3, out_channels=128, kernel_size=(3, 3))
        self.dropout = torch.nn.Dropout(0.2)
        self.sigmoid = torch.nn.Sigmoid()
        self.flatten = torch.nn.Flatten(1, 3)
        self.linear = torch.nn.Linear(in_features=1, out_features=1, bias=False)

    def forward(self, x):
        x1 = self.trconv(x)
        x = self.sigmoid(x1)
        x = self.dropout(x)
        x = x.unsqueeze(1)
        x = self.linear(x)
        return x




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (8448x66 and 1x1)

jit:
Failed running call_module L__self___linear(*(FakeTensor(..., device='cuda:0', size=(1, 1, 128, 66, 66)),), **{}):
a and b must have same reduction dim, but got [8448, 66] X [1, 1].

from user code:
   File "<string>", line 30, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''