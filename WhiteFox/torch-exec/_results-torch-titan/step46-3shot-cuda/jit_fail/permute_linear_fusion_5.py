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
        self.rnn = torch.nn.LSTM(1, 2, bias=True, dropout=0.3)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = self.rnn(v1)
        return v2[0].detach()




func = Model().to('cuda')



x1 = torch.randn(1, 2, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
shape '[16, 1]' is invalid for input of size 8

jit:
shape '[16, 1]' is invalid for input of size 8
'''