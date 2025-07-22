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

class M(torch.nn.Module):

    def __init__(self):
        super(M, self).__init__()
        self.dropout = torch.nn.Dropout(0.5)

    def forward(self, x):
        x = self.dropout(x)
        y = torch.rand_like(x)
        output = self.dropout(y)
        return output



func = M().to('cpu')

x = 1

test_inputs = [x]

# JIT_FAIL
'''
direct:
dropout(): argument 'input' (position 1) must be Tensor, not int

jit:
dropout(): argument 'input' (position 1) must be Tensor, not int
'''