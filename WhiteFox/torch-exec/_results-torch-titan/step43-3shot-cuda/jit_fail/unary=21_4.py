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



class ModelTanh(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.ConvTranspose1d(3, 10, 3, stride=1)
        self.conv2 = torch.nn.ConvTranspose2d(10, 3, 3, stride=1)

    def forward(self, x):
        v2 = self.conv1(x)
        v3 = torch.tanh(v2)
        v4 = self.conv2(v3)
        return torch.tanh(v4)




func = ModelTanh().to('cuda')



x = torch.randn(1, 3, 1, 1)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Expected 2D (unbatched) or 3D (batched) input to conv_transpose1d, but got input of size: [1, 3, 1, 1]

jit:
Failed running call_module L__self___conv1(*(FakeTensor(..., device='cuda:0', size=(1, 3, 1, 1)),), **{}):
Expected 2D (unbatched) or 3D (batched) input to conv_transpose1d, but got input of size: [1, 3, 1, 1]

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''