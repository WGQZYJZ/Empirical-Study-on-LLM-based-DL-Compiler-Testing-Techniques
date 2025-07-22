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

    def __init__(self, min_value=(- 10)):
        super().__init__()
        self.linear = torch.nn.Linear(784, 10, bias=True)

    def forward(self, x1):
        x11 = torch.reshape(x1, ((- 1), 784))
        v1 = self.linear(x11)
        v2 = torch.clamp_min(v1, min_value=min_value)
        v3 = torch.clamp_max(v2, max_value=10.5)
        return torch.argmax(v3, dim=1)



func = Model().to('cuda')



x1 = torch.randn(128, 28, 28)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
clamp_min() received an invalid combination of arguments - got (Tensor, min_value=int), but expected one of:
 * (Tensor input, Tensor min, *, Tensor out)
 * (Tensor input, Number min, *, Tensor out)


jit:
Failed running call_function <built-in method clamp_min of type object at 0x7464388699e0>(*(FakeTensor(..., device='cuda:0', size=(128, 10)),), **{'min_value': 1}):
clamp_min() received an invalid combination of arguments - got (FakeTensor, min_value=int), but expected one of:
 * (Tensor input, Tensor min, *, Tensor out)
 * (Tensor input, Number min, *, Tensor out)


from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''