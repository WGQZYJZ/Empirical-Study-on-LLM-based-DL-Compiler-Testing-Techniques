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
        self.layers = nn.Linear(2, 6)

    def forward(self, x):
        x = self.layers(x)
        x = torch.stack([x, x, x, x], dim=3)
        x = x.view(x.shape[0], (- 1))
        return x




func = Model().to('cuda')



x = torch.randn(2, 2)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Dimension out of range (expected to be in range of [-3, 2], but got 3)

jit:
Failed running call_function <built-in method stack of type object at 0x79d7e90699e0>(*([FakeTensor(..., device='cuda:0', size=(2, 6)), FakeTensor(..., device='cuda:0', size=(2, 6)), FakeTensor(..., device='cuda:0', size=(2, 6)), FakeTensor(..., device='cuda:0', size=(2, 6))],), **{'dim': 3}):
Dimension out of range (expected to be in range of [-3, 2], but got 3)

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''