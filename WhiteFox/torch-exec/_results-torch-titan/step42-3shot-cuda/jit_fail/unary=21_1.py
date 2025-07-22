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



class ModelTanh(nn.Module):

    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv1d(1, 200, 3, stride=2)
        self.conv2 = torch.nn.Conv2d(16, 32, 3, stride=1, bias=False)
        self.conv3 = torch.nn.Conv3d(16, 32, 3, stride=3, bias=False)
        self.conv4 = torch.nn.Conv2d(16, 8, kernel_size=2, stride=(2, 1))
        self.tanh = nn.Tanh()

    def forward(self, x):
        x = torch.tanh(self.conv1(x))
        x = torch.sigmoid(self.conv2(x))
        x = torch.relu(self.conv3(x))
        x = torch.tanh(self.conv4(x))
        x = self.tanh(x)
        return x




func = ModelTanh().to('cuda')



x = torch.randn(1, 1, 42, 287)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Expected 2D (unbatched) or 3D (batched) input to conv1d, but got input of size: [1, 1, 42, 287]

jit:
Failed running call_module L__self___conv1(*(FakeTensor(..., device='cuda:0', size=(1, 1, 42, 287)),), **{}):
Expected 2D (unbatched) or 3D (batched) input to conv1d, but got input of size: [1, 1, 42, 287]

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''