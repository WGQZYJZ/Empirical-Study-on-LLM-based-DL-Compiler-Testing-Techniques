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

    def forward(self):
        v = [torch.nn.functional.adaptive_avg_pool2d(torch.randn(5, 5, 3, 3), (5, 5)), torch.nn.functional.adaptive_avg_pool2d(torch.randn(5, 5, 3, 3), (4, 4)), torch.nn.functional.adaptive_avg_pool2d(torch.randn(5, 5, 3, 3), (3, 3)), torch.nn.functional.adaptive_avg_pool2d(torch.randn(5, 5, 3, 3), (5, 5)), torch.nn.functional.adaptive_avg_pool2d(torch.randn(5, 5, 3, 3), (4, 4)), torch.nn.functional.adaptive_avg_pool2d(torch.randn(5, 5, 3, 3), (3, 3))]
        return torch.cat(v, 0)




func = Model().to('cuda')

input_tensor = torch.randn(1, 1, 1)

test_inputs = [input_tensor]

# JIT_FAIL
'''
direct:
forward() takes 1 positional argument but 2 were given

jit:
forward() takes 1 positional argument but 2 were given
'''