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
        super(Model, self).__init__()
        self.conv2d_1a = torch.nn.ConvTranspose2d(1, 128, 1, stride=1)
        self.conv2d_2a = torch.nn.ConvTranspose2d(128, 256, 1, stride=1)
        self.conv2d_1d = torch.nn.ConvTranspose2d(128, 64, 1, stride=1)
        self.conv2d_2d = torch.nn.ConvTranspose2d(256, 256, 1, stride=1)
        self.conv2d_3d = torch.nn.ConvTranspose2d(256, 256, 1, stride=1)
        self.conv2d_1s = torch.nn.ConvTranspose2d(64, 1, 3, stride=1)
        self.conv2d_2s = torch.nn.ConvTranspose2d(256, 128, 3, stride=1)
        self.conv2d_3s = torch.nn.ConvTranspose2d(256, 1, 2, stride=1)

    def forward(self, input):
        x1 = self.conv2d_1a(input)
        x1 = self.conv2d_2a(x1)
        x1 = torch.unsqueeze(input, dim=1)
        x1 = torch.cat((x1, x1), dim=1)
        x2 = self.conv2d_1d(x1)
        x2 = self.conv2d_2d(x2)
        x2 = self.conv2d_3d(x2)
        x3 = self.conv2d_1s(x2)
        x3 = self.conv2d_2s(x3)
        x3 = self.conv2d_3s(x3)
        return x3




func = Model().to('cuda')



input = torch.randn(1, 1, 256, 256)


test_inputs = [input]

# JIT_FAIL
'''
direct:
Expected 3D (unbatched) or 4D (batched) input to conv_transpose2d, but got input of size: [1, 2, 1, 256, 256]

jit:
Failed running call_module L__self___conv2d_1d(*(FakeTensor(..., device='cuda:0', size=(1, 2, 1, 256, 256)),), **{}):
Expected 3D (unbatched) or 4D (batched) input to conv_transpose2d, but got input of size: [1, 2, 1, 256, 256]

from user code:
   File "<string>", line 33, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''