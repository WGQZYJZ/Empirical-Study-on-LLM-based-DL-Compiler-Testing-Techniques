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
        self.dropout1 = torch.nn.Dropout()
        self.dropout2 = torch.nn.Dropout(training=True)

    def forward(self, x1):
        x2 = self.dropout1(x1)
        x3 = self.dropout2(x1)
        return x3

class Model(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.dropout1 = torch.nn.Dropout()
        self.dropout2 = torch.nn.Dropout(training=True)

    def forward(self, x1):
        x2 = self.dropout1(x1)
        return x2

class Model(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.dropout1 = torch.nn.Dropout()

    def forward(self, x1):
        x2 = self.dropout1(x1)
        x3 = self.dropout1(x1, training=True)
        return x3

class Model(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.dropout1 = torch.nn.Dropout()

    def forward(self, x1):
        x2 = self.dropout1(x1, training=True)
        return x2



func = Model().to('cpu')


x1 = torch.randn(1, 2, 2)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
forward() got an unexpected keyword argument 'training'

jit:
forward() got an unexpected keyword argument 'training'
'''