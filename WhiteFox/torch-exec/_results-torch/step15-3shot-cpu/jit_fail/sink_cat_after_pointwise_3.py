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
        self.fc1 = torch.nn.Linear(2, 3)
        self.fc2 = torch.nn.Linear(3, 4)

    def forward(self, x1, x2):
        x3 = torch.cat((x1, x2), dim=0)
        y1 = self.fc1(x3)
        self.add_module('fc1', self.fc1)
        y2 = self.fc2(y1)
        self.add_module('fc2', self.fc2)
        return y3



func = Model().to('cpu')


x1 = torch.randn(1, 2)

x2 = torch.randn(1, 2)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
name 'y3' is not defined

jit:
NameError: name 'y3' is not defined

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''