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
        self.conv = torch.nn.Conv2d(1, 3, 1, stride=1, padding=1)

    def forward(self, x1, x2, argmax=None):
        v1 = torch.flatten(x1, 1)
        v2 = self.conv(v1)
        if (argmax == None):
            argmax = torch.argmax(v2, dim=0, keepdim=True)
        return (x2 + argmax)




func = Model().to('cuda')



x1 = torch.randn(1, 1, 3, 64, 64)



x2 = torch.randn(3, 64, 64)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Expected 3D (unbatched) or 4D (batched) input to conv2d, but got input of size: [1, 12288]

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(1, 12288)),), **{}):
Expected 3D (unbatched) or 4D (batched) input to conv2d, but got input of size: [1, 12288]

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''