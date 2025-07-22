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
        self.conv_transpose1 = torch.nn.modules.conv.ConvTranspose2d(in_channels=39, out_channels=64, kernel_size=(1, 11), stride=(2, 1), padding=(1, 0), output_padding=(1, 0))
        self.conv_transpose2 = torch.nn.modules.conv.ConvTranspose2d(in_channels=64, out_channels=64, kernel_size=(1, 9), stride=(8, 1), padding=(0, 0), output_padding=(0, 0))

    def forward(self, x1):
        v1 = self.conv_transpose1(x1)
        v2 = self.conv_transpose2(v1)
        v3 = torch.sigmoid(v2)
        return v3




func = Model().to('cuda')



x1 = torch.randn(1, 39, 1, 189)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Only zero batch or zero channel inputs are supported, but got input shape: [1, 64, 0, 199]

jit:
Failed running call_module L__self___conv_transpose2(*(FakeTensor(..., device='cuda:0', size=(1, 64, 0, 199)),), **{}):
Only zero batch or zero channel inputs are supported, but got input shape: [1, 64, 0, 199]

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''