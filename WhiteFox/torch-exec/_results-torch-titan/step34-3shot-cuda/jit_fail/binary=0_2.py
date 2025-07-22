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
        self.upsample = torch.nn.Upsample(mode='linear', scale_factor=None, align_corners=None)

    def forward(self, x, target):
        var = self.upsample(x, output_size=target.shape)
        output = (var + target)
        return output




func = Model().to('cuda')



x = torch.randn(1, 1, 2, 2, requires_grad=True)



target = torch.randn(2, 4, 2, 2)


test_inputs = [x, target]

# JIT_FAIL
'''
direct:
forward() got an unexpected keyword argument 'output_size'

jit:
Failed running call_module L__self___upsample(*(FakeTensor(..., device='cuda:0', size=(1, 1, 2, 2)),), **{'output_size': (2, 4, 2, 2)}):
forward() got an unexpected keyword argument 'output_size'

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''