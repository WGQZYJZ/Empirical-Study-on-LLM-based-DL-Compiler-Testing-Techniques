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

    def forward(self, input1, input2):
        t1 = torch.mm(input1, input1)
        t2 = (torch.mm(torch.mm(input1, input1), input2) + torch.mm(input1, input2))
        t3 = (torch.mm(input2, torch.mm(input1, input2)) + torch.mm(torch.mm(input1, input2), torch.mm(input1, input1)))
        t4 = (torch.mm(torch.mm(input2, torch.mm(input1, input2)), torch.mm(input1, input1)) + torch.mm(torch.mm(input2, torch.mm(input1, input1)), input2))
        t5 = (torch.mm(torch.mm(torch.mm(input2, torch.mm(input1, input2)), torch.mm(input1, input1)), torch.mm(input1, input1)) + torch.mm(torch.mm(torch.mm(input2, torch.mm(input1, input1)), torch.mm(input1, input2)), torch.mm(input1, input1)))
        t6 = (t1 - (t2 + ((t3 * t4) / t5)))
        return t6




func = Model().to('cuda')



input1 = torch.randn(8, 8)



input2 = torch.randn(8, 8)



input3 = torch.randn(8, 8)



input4 = torch.randn(7, 7)


test_inputs = [input1, input2, input3, input4]

# JIT_FAIL
'''
direct:
forward() takes 3 positional arguments but 5 were given

jit:
forward() takes 3 positional arguments but 5 were given
'''