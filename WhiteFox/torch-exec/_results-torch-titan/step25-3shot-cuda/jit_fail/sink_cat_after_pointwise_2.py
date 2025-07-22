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

    def forward(self, x):
        y = torch.concat((x, x), dim=1)
        aa = torch.reshape(y, 5, (- 1))
        bb = torch.tanh(aa)
        cc = torch.matmul(bb, bb.shape[0], bb.shape[0])
        return cc




func = Model().to('cuda')



x = torch.randn(5, 3, 4)



y = torch.randn(5, 3, 4)


test_inputs = [x, y]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 3 were given

jit:
forward() takes 2 positional arguments but 3 were given
'''