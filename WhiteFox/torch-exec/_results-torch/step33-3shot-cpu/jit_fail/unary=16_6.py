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
        self.linear1 = torch.nn.Linear(20, 10)
        self.linear2 = torch.nn.Linear(10, 2)

    def forward(self, x1):
        lin = self.linear1(x1)
        non_linear = relu(lin)
        return non_linear


func = Model().to('cpu')


x1 = torch.randn(1, 20)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
name 'relu' is not defined

jit:
NameError: name 'relu' is not defined

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''