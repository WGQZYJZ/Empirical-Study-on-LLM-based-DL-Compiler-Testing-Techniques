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

    def forward(self, x, y):
        x = torch.nn.functional.dropout(x, p=0.5, out=y)
        return x + 2



func = Model().to('cpu')


x1 = torch.randn(1, 2, 2)

y1 = torch.randn(1, 2, 2)

test_inputs = [x1, y1]

# JIT_FAIL
'''
direct:
dropout() got an unexpected keyword argument 'out'

jit:
dropout() got an unexpected keyword argument 'out'
'''