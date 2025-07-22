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

    def forward(self, input3, input4):
        return torch.cat([t2, torch.mm(input3, input4)], 1)




func = Model().to('cuda')



input1 = torch.randn(2, 2)



input2 = torch.randn(1, 2)



input3 = torch.randn(2, 1)



input4 = torch.randn(1, 2)


test_inputs = [input1, input2, input3, input4]

# JIT_FAIL
'''
direct:
forward() takes 3 positional arguments but 5 were given

jit:
forward() takes 3 positional arguments but 5 were given
'''