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

    def __init__(self, weight1, weight2):
        super(Model, self).__init__()
        self.weight1 = weight1
        self.weight2 = weight2
        self.weight3 = torch.randn(4, 4)

    def forward(self, input):
        t1 = torch.mm(input, self.weight1)
        t2 = torch.mm(input, self.weight2)
        t3 = torch.mm(self.weight3, self.weight3)
        t4 = torch.mm(input, self.weight2)
        t5 = (t1 * self.weight1)
        t6 = (torch.mm(t5, input) * self.weight1)
        t7 = (((t1 * t2) + t1) + t3)
        t8 = (t2 - t4)
        t9 = ((t7 * t8) + (t6 * t3))
        t11 = (t3 * t9)
        t12 = ((t3 * torch.mm(t1, input)) * t6)
        t13 = (t7 + t11)
        t14 = (t8 + t12)
        t15 = (t13 + t14)
        return t15




weight1 = torch.randn(2, 2)


weight2 = torch.randn(4, 4)


func = Model(weight1, weight2).to('cuda')



input = torch.randn(4, 4)



weight1 = torch.randn(2, 2)



weight2 = torch.randn(4, 4)


test_inputs = [input, weight1, weight2]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 4 were given

jit:
forward() takes 2 positional arguments but 4 were given
'''