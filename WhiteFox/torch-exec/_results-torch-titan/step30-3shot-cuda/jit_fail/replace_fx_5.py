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



class testModel(torch.nn.Module):

    def forward(x):
        o1 = torch.nn.functional.dropout(x, p=0.8)
        o2 = torch.rand_like(x)
        return o1




func = testModel().to('cuda')



x = torch.randn([])


test_inputs = [x]

# JIT_FAIL
'''
direct:
forward() takes 1 positional argument but 2 were given

jit:
forward() takes 1 positional argument but 2 were given
'''