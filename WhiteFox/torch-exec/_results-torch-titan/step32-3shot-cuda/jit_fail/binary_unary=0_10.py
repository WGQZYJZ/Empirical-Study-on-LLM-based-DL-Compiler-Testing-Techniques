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
        self.fc_0 = torch.nn.Linear(4, 4)
        self.fc_7 = torch.nn.Linear(4, 4)
        self.fc_8 = torch.nn.Linear(4, 4)

    def forward(self, x):
        v1 = torch.relu(self.fc_0(x))
        v4 = self.fc_7(v1)
        v8 = self.fc_8(v1)
        v9 = torch.pow(v4, v8)
        v10 = torch.nn.functional.log(v9)
        return v10




func = Model().to('cuda')



x = torch.randn(1, 4)


test_inputs = [x]

# JIT_FAIL
'''
direct:
module 'torch.nn.functional' has no attribute 'log'

jit:
module 'torch.nn.functional' has no attribute 'log'

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''