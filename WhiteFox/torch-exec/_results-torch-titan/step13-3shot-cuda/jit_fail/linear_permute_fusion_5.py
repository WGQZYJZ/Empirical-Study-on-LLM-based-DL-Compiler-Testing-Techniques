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



class A(torch.nn.Module):

    def __init__(self, A):
        super().__init__()
        self.A = A




class Model(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.module1 = A(torch.nn.Linear(1, 1))
        self.module2 = A(self.module1)

    def forward(self, input_tenosr):
        res = self.module1(input_tenosr)
        a1 = res.permute(0, 2, 1)
        return a1



func = Model().to('cuda')



x1 = torch.randn(1, 1, 1)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Module [A] is missing the required "forward" function

jit:
Module [A] is missing the required "forward" function
'''