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

    def forward(self, input):
        x = torch.mm(input, input) + torch.mm(input, input)
        x = torch.mm(input, input)
        t1 = torch.mm(input, input)
        t2 = torch.mm(input, input)
        t3 = torch.mm(input, input)
        t4 = torch.mm(input, input)
        t5 = torch.mm(input, input)
        x = torch.mm(input, input)
        x = torch.mm(input, input)
        x = torch.mm(input, input)
        return torch.mm(input, input) + torch.mm(input, input)



func = Model().to('cpu')


input1 = torch.randn(1, 1)

input2 = torch.randn(1, 1)

test_inputs = [input1, input2]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 3 were given

jit:
forward() takes 2 positional arguments but 3 were given
'''