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



class Conv2dReLU(torch.nn.Sequential):

    def __init__(self, c_in, c_out, **kwargs):
        super().__init__(torch.nn.Conv2d(c_in, c_out, **kwargs), torch.nn.ReLU6(inplace=False))




class Model(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 11, 3, stride=2, padding=1)
        self.model = torch.nn.Sequential(Conv2dReLU(2, 2, kernel_size=3, stride=2, padding=1), Conv2dReLU(2, 2, kernel_size=1, stride=1, padding=0), Conv2dReLU(2, 2, kernel_size=3, stride=2, padding=1))

    def forward(self, x, other=0.1):
        x = self.conv(x)
        x = F.adaptive_avg_pool2d(x, (1, 1))
        x = torch.flatten(x, 1)
        x = self.model(x)
        x = (x + 1.1)
        if (other == False):
            other = torch.randn(v1.shape)
        x = (x + other)
        return x




func = Model().to('cuda')



x1 = torch.randn(5, 3, 224, 224)

x = 1

test_inputs = [x1, x]

# JIT_FAIL
'''
direct:
Expected 3D (unbatched) or 4D (batched) input to conv2d, but got input of size: [5, 11]

jit:
Failed running call_module L__self___model_0_0(*(FakeTensor(..., device='cuda:0', size=(5, 11)),), **{}):
Expected 3D (unbatched) or 4D (batched) input to conv2d, but got input of size: [5, 11]

from user code:
   File "<string>", line 34, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''