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
        self.conv1 = torch.nn.Conv2d(1, 20, 5, 1)
        self.conv2 = torch.nn.Conv2d(20, 50, 5, 1)
        self.fc1 = torch.nn.Linear(((4 * 4) * 50), 500)
        self.fc2 = torch.nn.Linear(500, 10)

    def forward(self, x1, x2):
        y1 = self.conv1(x1)
        y2 = self.conv2(y1)
        y3 = F.relu(y2)
        y4 = y3.flatten(1)
        y5 = self.fc1(y4)
        y6 = self.fc2(y5)
        y7 = F.log_softmax(y6, dim=1)
        return (y7 + x2)




func = Model().to('cuda')



x1 = torch.randn(1, 1, 28, 28)



x2 = torch.randn(1)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x20000 and 800x500)

jit:
Failed running call_module L__self___fc1(*(FakeTensor(..., device='cuda:0', size=(1, 20000)),), **{}):
a and b must have same reduction dim, but got [1, 20000] X [800, 500].

from user code:
   File "<string>", line 29, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''