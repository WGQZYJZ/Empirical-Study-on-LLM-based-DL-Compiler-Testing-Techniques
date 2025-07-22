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
        self.linear = torch.nn.Linear(20, 10)

    def forward(self, x3):
        t2 = torch.clamp_min(t1, min_value=0)
        t3 = torch.clamp_max(t2, max_value=2)
        return t3


func = Model().to('cpu')

x3 = 1

test_inputs = [x3]

# JIT_FAIL
'''
direct:
name 't1' is not defined

jit:
NameError: name 't1' is not defined

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''