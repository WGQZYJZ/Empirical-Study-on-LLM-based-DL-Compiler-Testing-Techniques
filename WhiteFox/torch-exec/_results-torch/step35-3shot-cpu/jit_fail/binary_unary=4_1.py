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

    def __init__(self, other):
        super().__init__()
        self.linear = torch.nn.Linear(28, 10)
        self.other = torch.nn.Parameter(other)

    def forwark(self, x2):
        v1 = self.linear(x2)
        v2 = v1 + self.other
        v3 = torch.nn.functional.relu(v2)
        return v3


other = 1
func = Model(torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]).unsqueeze(0).unsqueeze(-1).unsqueeze(-1)).to('cpu')


x2 = torch.randn(1, 28, 1, 1)

test_inputs = [x2]

# JIT_FAIL
'''
direct:
Module [Model] is missing the required "forward" function

jit:
Module [Model] is missing the required "forward" function
'''