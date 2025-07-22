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

class Net(nn.Module):

    def forward(self, x1, x2):
        return -torch.matmul(x1, x2)



func = Net().to('cpu')


w = torch.randn(3, 3)

x1 = torch.randn(4, 5)

x2 = torch.randn(5, 7)

test_inputs = [w, x1, x2]

# JIT_FAIL
'''
direct:
forward() takes 3 positional arguments but 4 were given

jit:
forward() takes 3 positional arguments but 4 were given
'''