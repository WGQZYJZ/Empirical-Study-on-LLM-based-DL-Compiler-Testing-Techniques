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
        self.input1 = torch.randn(2, 2)
        self.model1 = torch.nn.Sequential(torch.nn.ReLU(), torch.nn.Linear(2, 2), torch.nn.PReLU(), torch.nn.BatchNorm1d(2), torch.nn.Dropout(0.1), torch.nn.Softmax(), torch.nn.Sigmoid(), torch.nn.GELU(), torch.nn.ReLU(), torch.nn.LeakyReLU(), torch.nn.Softplus(), torch.nn.Tanh())

    def forward(self):
        x1 = self.input1
        x2 = self.model1(x1)
        return (x1, x2)




func = Model().to('cuda')

input_tensor = torch.randn(1, 1, 1)

test_inputs = [input_tensor]

# JIT_FAIL
'''
direct:
forward() takes 1 positional argument but 2 were given

jit:
forward() takes 1 positional argument but 2 were given
'''