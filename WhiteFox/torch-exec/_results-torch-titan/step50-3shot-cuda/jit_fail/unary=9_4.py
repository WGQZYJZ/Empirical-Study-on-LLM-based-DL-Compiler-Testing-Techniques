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
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.other_conv = torch.nn.Conv2d(8, 8, 1, stride=2, padding=1)

    def forward(self, x1):
        v1 = self.conv(x1)
        v1 = torch.add(v1, 3)
        v2 = torch.clamp(v1, 0, 6)
        v3 = torch.div(v2, 6)
        v4 = self.other_conv(v3)
        v4 = torch.add_(v4, 3)
        v5 = torch.clamp_(v4, 0, 6)
        v6 = torch.div_(v5, 6)
        return v6




func = Model().to('cuda')



x1 = torch.randn(5, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
module 'torch' has no attribute 'add_'

jit:
module 'torch' has no attribute 'add_'

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''