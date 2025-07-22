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



class ModelTanh(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.relu = torch.nn.ReLU(inplace=False)
        self.conv1d = torch.nn.Conv1d(16, 64, 1, bias=False)

    def forward(self, x):
        t1 = self.relu(x)
        t2 = self.conv1d(t1)
        t3 = torch.tanh(t2)
        y1 = nn.Sigmoid(t3)
        return y1




func = ModelTanh().to('cuda')



x = torch.randn(128, 16, 40)


test_inputs = [x]

# JIT_STATUS
'''
direct:
Sigmoid.__init__() takes 1 positional argument but 2 were given

jit:

'''