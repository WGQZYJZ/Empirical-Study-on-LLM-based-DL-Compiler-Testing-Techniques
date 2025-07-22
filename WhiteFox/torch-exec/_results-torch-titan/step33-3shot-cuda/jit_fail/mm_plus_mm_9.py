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
        t1 = torch.mm(input, input)
        t2 = torch.mm(t1, input)
        t3 = torch.mm(input, t2)
        return (((t1 + t2) + t3) / 6)




func = Model().to('cuda')



input1 = torch.randn(2, 3)



input2 = torch.randn(3, 2)



input3 = torch.randn(2, 2)



input4 = torch.randn(3, 3)


test_inputs = [input1, input2, input3, input4]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 5 were given

jit:
forward() takes 2 positional arguments but 5 were given
'''