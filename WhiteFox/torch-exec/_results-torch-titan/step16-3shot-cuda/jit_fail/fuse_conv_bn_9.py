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



class Model(nn.Module):

    def __init__(self):
        super(Model, self).__init__()
        self.layer = nn.Sequential(nn.Conv3d(3, 3, kernel_size=3, stride=1, padding=1), nn.BatchNorm3d(3, eps=1e-05, momentum=0.1, affine=True), nn.Conv2d(3, 3, kernel_size=3, stride=1, padding=1), nn.BatchNorm2d(3, eps=1e-05, momentum=0.1, affine=True), nn.ReLU())

    def forward(self, x):
        return self.layer(x)




func = Model().to('cuda')



x = torch.randn(1, 3, 4, 4, 4)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Expected 3D (unbatched) or 4D (batched) input to conv2d, but got input of size: [1, 3, 4, 4, 4]

jit:
Failed running call_module L__self___layer_2(*(FakeTensor(..., device='cuda:0', size=(1, 3, 4, 4, 4)),), **{}):
Expected 3D (unbatched) or 4D (batched) input to conv2d, but got input of size: [1, 3, 4, 4, 4]

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''