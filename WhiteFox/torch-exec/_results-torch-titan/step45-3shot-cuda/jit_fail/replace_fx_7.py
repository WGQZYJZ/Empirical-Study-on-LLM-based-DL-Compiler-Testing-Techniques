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
        t0 = torch.rand(1)
        t1 = torch.nn.functional.dropout(t0)
        t2 = torch.rand_like(t0)
        t3 = (t2 + t1)

    def forward(self):
        ...




func = Model().to('cuda')



dummy_input = torch.randn(1, 2, 2)


test_inputs = [dummy_input]

# JIT_FAIL
'''
direct:
forward() takes 1 positional argument but 2 were given

jit:
forward() takes 1 positional argument but 2 were given
'''