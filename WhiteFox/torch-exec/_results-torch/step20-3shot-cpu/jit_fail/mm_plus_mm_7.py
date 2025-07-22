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

    def forward(self, input1, input2, input3, input4, input5, input6):
        mm1 = torch.mm(input1, input3)
        mm2 = torch.mm(input5, input3)
        mm3 = torch.mm(input2, input4)
        mm4 = torch.mm(input6, input4)
        t = mm1 + mm2
        u = mm3 + mm4
        return torch.mm(t, u)



func = Model().to('cpu')


mm1 = torch.randn(55, 55)

input2 = torch.randn(55, 55)

input3 = torch.randn(55, 55)

input4 = torch.randn(55, 55)

mm3 = torch.randn(55, 55)

input5 = torch.randn(55, 55)

input6 = torch.randn(55, 55)

test_inputs = [mm1, input2, input3, input4, mm3, input5, input6]

# JIT_FAIL
'''
direct:
forward() takes 7 positional arguments but 8 were given

jit:
forward() takes 7 positional arguments but 8 were given
'''