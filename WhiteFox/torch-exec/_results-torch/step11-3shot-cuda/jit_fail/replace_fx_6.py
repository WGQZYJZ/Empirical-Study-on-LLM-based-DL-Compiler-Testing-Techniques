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

class model(torch.nn.Module):

    def __init__(self):
        super().__init__()

    def forward(self, x, y=None):
        c1 = torch.nn.functional.dropout(y, p=0.2)
        return 1



func = model().to('cuda')


x1 = torch.randn(1)
x = 1

test_inputs = [x1, x]

# JIT_FAIL
'''
direct:
dropout(): argument 'input' (position 1) must be Tensor, not int

jit:
dropout(): argument 'input' (position 1) must be Tensor, not int
'''