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
        self.fc1 = torch.nn.Linear((64 * 64), 64)
        self.fc2 = torch.nn.Linear(64, 1)

    def forward(self, x1):
        v1 = torch.reshape(input_tensor, (1, (64 * 64)))
        v2 = torch.nn.functional.relu(self.fc1(v1))
        v3 = self.fc2(v2)
        y1 = torch.reshape(v3, (1,))
        return y1



func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
name 'input_tensor' is not defined

jit:
name 'input_tensor' is not defined

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''