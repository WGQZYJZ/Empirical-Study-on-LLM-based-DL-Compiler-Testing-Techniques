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

    def __init__(self, min, max):
        super().__init__()
        self.max = max
        self.min = min
        self.linear = torch.nn.Linear(1, 1)

    def forward(self, x1):
        v1 = x1[0]
        v2 = v1.size()
        v3 = torch.empty((v2[0] * v2[1]), 1, device=v1.device, dtype=v1.dtype)
        if (v3.numel() > 0):
            torch.nn._functions.thnn.batchnorm_backward_reduce(v2, v3, v1, torch.tensor(0.09241063170719147, device=v1.device, requires_grad=True, dtype=torch.float64), torch.tensor((- 0.6326493716239929), device=v1.device, requires_grad=True, dtype=torch.float32), torch.tensor(10.488529205322266, device=v1.device, requires_grad=True, dtype=torch.float32), torch.ones(v2[0], requires_grad=False, device=v1.device, dtype=torch.float32), True)
        v4 = v3.reshape(v2)
        v5 = self.linear(v4)
        v6 = torch.clamp_min(v5, self.min)
        v7 = torch.clamp_max(v6, self.max)
        return v7




min = 0.959989


max = 0.408781


func = Model(min, max).to('cuda')



x1 = torch.randn(4, 3, 512)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
module 'torch.nn' has no attribute '_functions'

jit:
module 'torch.nn' has no attribute '_functions'

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''