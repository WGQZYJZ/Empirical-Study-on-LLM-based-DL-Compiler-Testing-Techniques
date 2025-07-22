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

    def __init__(self, weight=torch.tensor([[(- 1.2), 4.2, 5.2, 0.2], [2.5, 2.4, 10.0, 1.8], [(- 1.5), (- 0.5), 2.7, (- 3.0)], [1.2, (- 3.2), 1.5, 1.3]])):
        super().__init__()
        self.linear = torch.nn.Linear(4, 4)
        self.linear.weight = torch.nn.Parameter(weight)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = (v1 + y)
        v3 = nn.functional.relu(v2)
        return v3



func = Model().to('cuda')



x1 = torch.randn(1, 4)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
name 'y' is not defined

jit:
name 'y' is not defined

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''