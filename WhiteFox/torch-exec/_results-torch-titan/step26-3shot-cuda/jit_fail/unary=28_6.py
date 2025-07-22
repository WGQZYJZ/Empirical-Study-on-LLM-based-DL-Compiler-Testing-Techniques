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

    def __init__(self, min_value, max_value):
        super().__init__()
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x1):
        v1 = x1.reshape(x1.size(0), ((64 * 64) * 3))
        v2 = torch.nn.functional.linear(v1, torch.ones(16369))
        v3 = torch.clamp_min(v2, self.min_value)
        v4 = torch.clamp_max(v3, self.max_value)
        return v4




min_value = 136


max_value = 8438

func = Model(min_value, max_value).to('cuda')



x1 = torch.zeros(2, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cpu and cuda:0! (when checking argument for argument mat in method wrapper_CUDA_addmv_)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., device='cuda:0', size=(2, 12288)), FakeTensor(..., size=(16369,))), **{}):
size mismatch, got input (2x12288), vec (16369)

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''