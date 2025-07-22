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
        self.linear1 = torch.nn.Linear(10, 10)
        self.linear2 = torch.nn.Linear(10, 10)

    def forward(self, x1):
        t1 = self.l1(x1)
        v1 = t1.tanh()
        return v1


func = Model().to('cpu')


x1 = torch.randn(1, 10)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
'Model' object has no attribute 'l1'

jit:
'Model' object has no attribute 'l1'
'''