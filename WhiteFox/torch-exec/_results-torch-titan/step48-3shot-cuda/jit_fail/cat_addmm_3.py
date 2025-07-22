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
        x = torch.mul(2, x)
        x = torch.stack(x)
        return x




func = Model().to('cuda')



x = torch.randn(2, 2)


test_inputs = [x]

# JIT_FAIL
'''
direct:
stack(): argument 'tensors' (position 1) must be tuple of Tensors, not Tensor

jit:
Failed running call_function <built-in method stack of type object at 0x7154814699e0>(*(FakeTensor(..., device='cuda:0', size=(2, 2)),), **{}):
stack(): argument 'tensors' (position 1) must be tuple of Tensors, not FakeTensor

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''