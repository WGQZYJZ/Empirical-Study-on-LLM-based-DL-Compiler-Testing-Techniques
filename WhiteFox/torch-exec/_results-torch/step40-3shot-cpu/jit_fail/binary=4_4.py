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

class MyModel(torch.nn.Module):

    def __init__(self):
        super().__init__()

    def forward(self, input_tensor, other):
        t1 = self.linear(input_tensor)
        return t1 + other


func = MyModel().to('cpu')


input_tensor = torch.randn(1, 3, 64, 64)

other = torch.zeros(1, 3, 64, 64)

test_inputs = [input_tensor, other]

# JIT_FAIL
'''
direct:
'MyModel' object has no attribute 'linear'

jit:
'MyModel' object has no attribute 'linear'
'''