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
        self.seq_len = 512

    def forward(self, x):
        x = x + x
        output = F.relu(x)
        return output



func = Model().to('cpu')

x = 1

test_inputs = [x]

# JIT_FAIL
'''
direct:
relu(): argument 'input' (position 1) must be Tensor, not int

jit:
relu(): argument 'input' (position 1) must be Tensor, not int
'''