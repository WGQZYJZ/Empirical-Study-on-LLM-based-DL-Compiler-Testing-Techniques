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
        self.conv_transpose = torch.nn.ConvTranspose2d(16, 32, 3, padding=1, stride=2)
        self.max_pool = torch.nn.MaxPool2d(4, return_indices=True)

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = torch.relu(v1)
        (v3, v4) = torch.max_pool(v2, 4)
        return v4




func = Model().to('cuda')



x1 = torch.randn(1, 16, 512, 512)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
module 'torch' has no attribute 'max_pool'

jit:
module 'torch' has no attribute 'max_pool'

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''