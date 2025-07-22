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

    def __init__(self, min_value, max_value):
        super().__init__()

    def forward(input_tensor):
        t1 = torch.tanh(input_tensor)
        t2 = torch.nn.functional.gelu(t1)
        t3 = torch.clamp_min(t2, min_value)
        k6 = torch.clamp_max(t3, max_value)
        return torch.sigmoid(k6)



min_value = 1
max_value = 1

func = Model(min_value, max_value).to('cuda')



x = torch.randn(2, 2, 2)


test_inputs = [x]

# JIT_FAIL
'''
direct:
forward() takes 1 positional argument but 2 were given

jit:
forward() takes 1 positional argument but 2 were given
'''