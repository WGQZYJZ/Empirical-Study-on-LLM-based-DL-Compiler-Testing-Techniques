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
        self.conv = torch.nn.Conv2d(5, 8, 1, stride=1, padding=1, dilation=1)

    def forward(self, x1_X0):
        v19 = self.conv(x1_X0)
        v20 = (2 + v19)
        v21 = torch.ops.aten.opset11.clamp(v20, 0, 6)
        v22 = (v21 / 6)
        return v22




func = Model().to('cuda')



x1_X0 = torch.randn(1, 5, 64, 64)


test_inputs = [x1_X0]

# JIT_FAIL
'''
direct:
'_OpNamespace' 'aten' object has no attribute 'opset11'

jit:
'_OpNamespace' 'aten' object has no attribute 'opset11'

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''