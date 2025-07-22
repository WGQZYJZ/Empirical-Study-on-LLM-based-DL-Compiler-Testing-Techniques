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
        self.conv1 = torch.nn.Conv2d(2, 2, 2)
        self.conv2 = torch.nn.Conv2d(2, 2, 2)

    def forward(self, x2):
        y = torch.nn.functional.batch_norm(self.conv1(x2), self.conv2(x2))
        return y




func = Model().to('cuda')



x2 = torch.randn(1, 2, 4, 4)


test_inputs = [x2]

# JIT_FAIL
'''
direct:
batch_norm() missing 1 required positional argument: 'running_var'

jit:
Failed running call_function <function batch_norm at 0x79e516fa3b80>(*(FakeTensor(..., device='cuda:0', size=(1, 2, 3, 3)), FakeTensor(..., device='cuda:0', size=(1, 2, 3, 3))), **{}):
batch_norm() missing 1 required positional argument: 'running_var'

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''