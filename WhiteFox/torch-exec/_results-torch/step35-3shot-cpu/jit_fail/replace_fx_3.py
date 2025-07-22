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

    def forward(self, x1):
        x2 = torch.zeros_like(x1, dtype=torch.float, device=torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu'))
        x3 = torch.rand_like(x1, dtype=torch.float, device=torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu'))
        x4 = torch.rand_like(x1, dtype=torch.float, device=torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu'))



func = Model().to('cpu')

x1 = 1

test_inputs = [x1]

# JIT_FAIL
'''
direct:
zeros_like(): argument 'input' (position 1) must be Tensor, not int

jit:
zeros_like(): argument 'input' (position 1) must be Tensor, not int
'''