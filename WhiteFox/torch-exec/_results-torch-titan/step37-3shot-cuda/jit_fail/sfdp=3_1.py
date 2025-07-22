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
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, input):
        q = self.linear_q(input)
        k = self.linear_k(input)
        v = self.linear_v(input)




func = Model().to('cuda')

input = 1

test_inputs = [input]

# JIT_FAIL
'''
direct:
'Model' object has no attribute 'linear_q'

jit:
linear_q

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''