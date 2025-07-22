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

    def forward(self, inp):
        v1 = torch.mul(torch.mul(input1, input2), input3)
        v2 = (v1 ** 2)
        return v2




func = Model().to('cuda')



inp = torch.randn(6)


test_inputs = [inp]

# JIT_FAIL
'''
direct:
name 'input1' is not defined

jit:
name 'input1' is not defined

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''