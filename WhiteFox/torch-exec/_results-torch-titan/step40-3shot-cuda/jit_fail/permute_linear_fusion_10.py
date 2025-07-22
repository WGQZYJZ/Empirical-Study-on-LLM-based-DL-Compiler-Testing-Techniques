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
        self.relu1 = torch.nn.ReLU()
        self.relu2 = torch.nn.ReLU()

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        v3 = v2.detach()
        v4 = torch.max(v3, dim=(- 1))[1]
        v4 = v4.unsqueeze(dim=(- 1))
        v3 = (v3 + v4)
        v4 = (v3 == 0).to(v3.dtype)
        v3 = v3.permute(0, 2, 1)
        v4 = torch.nn.functional.linear(v3, torch.nn.functional.relu(self.linear2.weight), torch.nn.functional.relu(self.linear2.bias))
        v4 = torch.sum(torch.nn.functional.hardtanh(v4, (- 1.0), 1.0))
        return v4




func = Model().to('cuda')



x1 = torch.randn(1, 2, 2)



x2 = torch.randn(1, 2, 2)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
'Model' object has no attribute 'linear'

jit:
linear

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''