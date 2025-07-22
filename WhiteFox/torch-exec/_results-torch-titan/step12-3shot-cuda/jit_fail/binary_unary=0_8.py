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
        self.conv1 = torch.nn.Conv2d(16, 16, 7, stride=1, padding=3)
        self.conv2 = torch.nn.Conv2d(16, 16, 7, stride=1, padding=3)

    def forward(self, x1, x2):
        v1 = self.conv1(x1)
        v2 = (x1 + v1)
        v3 = torch.relu(v2)
        v4 = torch.sum(v3)
        v5 = torch.relu(((v4 + v2) + v1), dim=0)
        v6 = self.conv2(v5)
        return (x2 + v6)




func = Model().to('cuda')



x1 = torch.randn(1, 16, 64, 64)



x2 = torch.randn(1, 16, 64, 64)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
relu() got an unexpected keyword argument 'dim'

jit:
Failed running call_function <built-in method relu of type object at 0x7f336ba699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 16, 64, 64)),), **{'dim': 0}):
relu() got an unexpected keyword argument 'dim'

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''