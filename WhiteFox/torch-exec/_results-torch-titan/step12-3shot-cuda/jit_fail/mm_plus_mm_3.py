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



class model(torch.nn.Module):

    def forward(self):
        t1 = torch.mm(input1, input2)
        t2 = torch.mm(input3, input4)
        t3 = (t1 + t2)
        return t3




func = model().to('cuda')



input1 = torch.randn(5, 5)



input2 = torch.randn(5, 5)



input3 = torch.randn(5, 5)



input4 = torch.randn(5, 5)


test_inputs = [input1, input2, input3, input4]

# JIT_FAIL
'''
direct:
forward() takes 1 positional argument but 5 were given

jit:
forward() takes 1 positional argument but 5 were given
'''