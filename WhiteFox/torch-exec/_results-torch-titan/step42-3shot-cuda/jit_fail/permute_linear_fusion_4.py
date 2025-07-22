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
        self.linear1 = torch.nn.Linear(2, 2)
        self.linear2 = torch.nn.Linear(2, 2)

    def forward(self, x1):
        y = self.flatten(x1)
        return torch.nn.functional.relu(torch.nn.functional.linear(y, self.linear1.weight, self.linear1.bias))




func = Model().to('cuda')



x1 = torch.randn(1, 1, 2, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
'Model' object has no attribute 'flatten'

jit:
flatten

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''