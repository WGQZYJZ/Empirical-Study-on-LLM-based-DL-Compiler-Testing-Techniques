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
        self.linear1 = torch.nn.Linear(1536, 10)

    def forward(self, x1):
        x1 = nn.Linear(in_features, out_features)(x1)
        x1 = torch.sigmoid(x1)
        x1 = torch.softmax(x1, dim=0)
        return x1


func = Model().to('cpu')


x1 = torch.randn(5, 1536)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
name 'in_features' is not defined

jit:
NameError: name 'in_features' is not defined

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''