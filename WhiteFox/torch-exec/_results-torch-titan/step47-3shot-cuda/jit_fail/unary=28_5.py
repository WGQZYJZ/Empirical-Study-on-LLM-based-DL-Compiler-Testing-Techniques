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
        self.dense = torch.nn.Linear(64, 128)

    def forward(self, x1, min_value=0, max_value=0.5):
        v1 = torch.clamp_max(self.dense(x1), min_value=min_value)
        return torch.clamp_max(v1, max_value=max_value)



func = Model().to('cuda')



x1 = torch.randn(1, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
clamp_max() received an invalid combination of arguments - got (Tensor, min_value=int), but expected one of:
 * (Tensor input, Tensor max, *, Tensor out)
 * (Tensor input, Number max, *, Tensor out)


jit:
Failed running call_function <built-in method clamp_max of type object at 0x7931a92699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 128)),), **{'min_value': 0}):
clamp_max() received an invalid combination of arguments - got (FakeTensor, min_value=int), but expected one of:
 * (Tensor input, Tensor max, *, Tensor out)
 * (Tensor input, Number max, *, Tensor out)


from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''