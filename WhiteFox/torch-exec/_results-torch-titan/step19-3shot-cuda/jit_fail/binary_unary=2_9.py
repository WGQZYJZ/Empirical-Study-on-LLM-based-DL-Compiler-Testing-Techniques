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
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
        self.fc = torch.nn.Linear(64, 1)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = v1.view((- 1), 64)
        v3 = self.fc(v2)
        v4 = torch.matmul((- 0.005), v1)
        return (v3 + v4)




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
matmul(): argument 'input' (position 1) must be Tensor, not float

jit:
Failed running call_function <built-in method matmul of type object at 0x7792ba2699e0>(*(-0.005, FakeTensor(..., device='cuda:0', size=(1, 8, 64, 64))), **{}):
matmul(): argument 'input' (position 1) must be Tensor, not float

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''