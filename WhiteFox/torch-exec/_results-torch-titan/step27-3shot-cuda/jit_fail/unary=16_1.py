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
        self.ln = torch.nn.Linear(1, 1)

    def forward(self, x):
        output = self.ln(x)
        output = relu(output)
        return output



func = Model().to('cuda')



x = torch.randn(1, 1)


test_inputs = [x]

# JIT_FAIL
'''
direct:
name 'relu' is not defined

jit:
name 'relu' is not defined

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''