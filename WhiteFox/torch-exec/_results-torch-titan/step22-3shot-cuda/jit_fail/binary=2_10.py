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
        self.conv = torch.nn.Conv1d(3, 16, 1, stride=1, padding=1)

    def forward(self, x):
        v1 = self.conv(x)
        v2 = (v1 - torch.tensor([0.754, 0.12123, 0.8424, 0.2234, 0.7123, 0.934], dtype=torch.float32).reshape((6, 1, 1)).to(device))
        return v2




func = Model().to('cuda')



x = torch.randn(1, 3, 32)


test_inputs = [x]

# JIT_FAIL
'''
direct:
name 'device' is not defined

jit:
name 'device' is not defined

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''