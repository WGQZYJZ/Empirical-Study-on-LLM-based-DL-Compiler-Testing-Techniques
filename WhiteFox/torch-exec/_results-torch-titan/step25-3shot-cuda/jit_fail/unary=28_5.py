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
        self.fc = torch.nn.Linear(768, 256)

    def forward(self, x1):
        v1 = self.fc(x1)
        v2 = torch.clamp_min(v1, min_value=0.05)
        v3 = torch.clamp_max(v2, max_value=0.8)
        return v3



func = Model().to('cuda')



x1 = torch.randn(1, 768)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
clamp_min() received an invalid combination of arguments - got (Tensor, min_value=float), but expected one of:
 * (Tensor input, Tensor min, *, Tensor out)
 * (Tensor input, Number min, *, Tensor out)


jit:
Failed running call_function <built-in method clamp_min of type object at 0x722f30e699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 256)),), **{'min_value': 0.05}):
clamp_min() received an invalid combination of arguments - got (FakeTensor, min_value=float), but expected one of:
 * (Tensor input, Tensor min, *, Tensor out)
 * (Tensor input, Number min, *, Tensor out)


from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''