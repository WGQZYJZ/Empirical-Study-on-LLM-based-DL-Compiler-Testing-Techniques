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



class Model(torch.nn.Sequential):

    def __init__(self):
        super().__init__(torch.nn.Linear(3, 8), torch.nn.ReLU(), torch.nn.Linear(8, 3), torch.nn.ReLU())
        self.min_value = (- 1000)
        self.max_value = 0

    def clamp(self, x):
        return x.clamp(self.min_value, self.max_value)

    def forward(self, x1):
        x2 = self.clamp(self.clamp(self.linear1_0(x1)))
        return self.clamp(self.clamp(self.linear1_3(x2)))



func = Model().to('cuda')



x1 = torch.randn(1, 3)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
'Model' object has no attribute 'linear1_0'

jit:
linear1_0

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''