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

    def __init__(self, input1, input2, input3, input4):
        super().__init__()
        self.w1 = torch.nn.Parameter(torch.randn(input1.size(), requires_grad=True))
        self.w2 = torch.nn.Parameter(torch.randn(input2.size(), requires_grad=True))
        self.w3 = torch.nn.Parameter(torch.randn(input3.size(), requires_grad=True))
        self.w4 = torch.nn.Parameter(torch.randn(input4.size(), requires_grad=True))

    def forward(self):
        v1 = torch.mm(self.w1, self.w2)
        v2 = torch.mm(self.w3, self.w4)
        v3 = (v1 + v2)
        return v3




input1 = torch.randn(5, 5)


input2 = torch.randn(5, 5)


input3 = torch.randn(5, 5)


input4 = torch.randn(5, 5)


func = Model(input1, input2, input3, input4).to('cuda')



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