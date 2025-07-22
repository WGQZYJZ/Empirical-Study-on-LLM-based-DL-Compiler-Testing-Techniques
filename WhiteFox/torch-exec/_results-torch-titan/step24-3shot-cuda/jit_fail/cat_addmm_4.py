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



class Model(nn.Module):

    def __init__(self):
        super().__init__()
        self.layers = nn.Linear(2, 4)

    def forward(self, x):
        x = self.layers(x)
        x = torch.flatten(x.split(2), start_dim=1)
        return x




func = Model().to('cuda')



x = torch.randn(2, 2)


test_inputs = [x]

# JIT_FAIL
'''
direct:
flatten(): argument 'input' (position 1) must be Tensor, not tuple

jit:
Failed running call_function <built-in method flatten of type object at 0x7678b38699e0>(*((FakeTensor(..., device='cuda:0', size=(2, 4)),),), **{'start_dim': 1}):
flatten(): argument 'input' (position 1) must be Tensor, not tuple

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''