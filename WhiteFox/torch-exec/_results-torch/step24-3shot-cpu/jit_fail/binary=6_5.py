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

    def forward(self, input_tensor):
        output = torch.nn.functional.linear(input=input_tensor, weight=None, bias=None) - other
        return output


func = Model().to('cpu')


x = torch.randn(1, 2)

y = torch.randn(1, 2)

test_inputs = [x, y]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 3 were given

jit:
forward() takes 2 positional arguments but 3 were given
'''