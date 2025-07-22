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

    def __init__(self, p1):
        super().__init__()
        self.a1 = torch.nn.functional.dropout(p1)
        self.a2 = torch.nn.functional.dropout(p1)

    def forward(self, x):
        x = self.a1(x) + self.a2(x)
        x = torch.nn.functional.dropout(x, p=0.8, training=False)
        x = torch.nn.functional.dropout(x, p=0.9, training=False)
        x = torch.rand_like(x)
        return 1


p1 = torch.randn(1, requires_grad=True)

func = Model(p1).to('cpu')


p1 = torch.randn(1, requires_grad=True)

test_inputs = [p1]

# JIT_FAIL
'''
direct:
'Tensor' object is not callable

jit:
'Tensor' object is not callable
'''