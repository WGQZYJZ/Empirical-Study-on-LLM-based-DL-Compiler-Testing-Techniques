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

    def __init__(self, input_data, weightings):
        super(Model, self).__init__()

    def forward(self, input_data):
        return torch.mm(input_data, self.weightings)


input_data = torch.randn(5, 5)
weightings = torch.randn(5, 5)

func = Model(input_data, weightings).to('cpu')


input_data = torch.randn(5, 5)

weightings = torch.randn(5, 5)

test_inputs = [input_data, weightings]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 3 were given

jit:
forward() takes 2 positional arguments but 3 were given
'''