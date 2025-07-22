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

    def forward(self, input1, input2, input3, input4):
        t = input1.mm(input2)
        t1 = t.mm(input3)
        t2 = t.mm(input4)
        t3 = torch.mm((t1 + t2), input2.mm(input4))
        return t3




func = Model().to('cuda')



x = torch.randn(2, 2)



y = torch.randn(2, 2)



z = torch.randn(2, 2)



u = torch.randn(2, 2)



mm = torch.randn(2, 2)


test_inputs = [x, y, z, u, mm]

# JIT_FAIL
'''
direct:
forward() takes 5 positional arguments but 6 were given

jit:
forward() takes 5 positional arguments but 6 were given
'''