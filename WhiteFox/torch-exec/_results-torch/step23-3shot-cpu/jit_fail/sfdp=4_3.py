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
        self.multihead_attn = None

    def forward(self, x1, x2):
        v1 = self.multihead_attn(x1, x2, x2)
        return v1


func = Model().to('cpu')

x1 = 1
x2 = 1

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
'NoneType' object is not callable

jit:
'NoneType' object is not callable
'''