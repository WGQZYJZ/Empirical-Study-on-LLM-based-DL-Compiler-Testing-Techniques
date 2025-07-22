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
        self.conv1 = torch.nn.ConvTranspose3d(1, 10, kernel_size=(2, 4, 6), stride=(2, 2, 2))
        self.conv2 = torch.nn.ConvTranspose3d(10, 20, kernel_size=(2, 3, 5), stride=(1, 3, 1))
        self.conv3 = torch.nn.ConvTranspose3d(20, 1, kernel_size=(2, 2, 4), stride=(1, 3, 4))

    def forward(self, x0):
        v0 = self.conv1(x0)
        v1 = torch.relu(v0)
        v2 = self.conv2(v1)
        v3 = torch.sigmoid(v2)
        v4 = self.conv3(torch.unsqueeze(v3, dim=0))
        return torch.tanh(torch.squeeze(v4, dim=0))




func = Model().to('cuda')



x0 = torch.randn(1, 1, 16, 32, 32)


test_inputs = [x0]

# JIT_FAIL
'''
direct:
Expected 4D (unbatched) or 5D (batched) input to conv_transpose3d, but got input of size: [1, 1, 20, 33, 198, 72]

jit:
Failed running call_module L__self___conv3(*(FakeTensor(..., device='cuda:0', size=(1, 1, 20, 33, 198, 72)),), **{}):
Expected 4D (unbatched) or 5D (batched) input to conv_transpose3d, but got input of size: [1, 1, 20, 33, 198, 72]

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''