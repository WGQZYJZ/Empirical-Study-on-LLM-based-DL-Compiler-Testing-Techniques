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
        self.l1 = nn.ConvTranspose2d(32, 64, kernel_size=(1, 1), stride=(1, 1))

    def forward(self, x):
        o1 = self.l1(x)
        o2 = nn.Sigmoid(o1)
        return o2




func = Model().to('cuda')



x = torch.randn(1, 32, 32, 32)


test_inputs = [x]

# JIT_STATUS
'''
direct:
Sigmoid.__init__() takes 1 positional argument but 2 were given

jit:

'''