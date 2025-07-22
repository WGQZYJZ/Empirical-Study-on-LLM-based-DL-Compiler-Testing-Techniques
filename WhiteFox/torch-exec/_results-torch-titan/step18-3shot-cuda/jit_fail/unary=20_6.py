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



class Net(nn.Module):

    def __init__(self):
        super().__init__()
        self.conv_1 = nn.ConvTranspose2d(32, 32, kernel_size=3, stride=1, padding=(1, 1), bias=False)

    def forward():
        pass




func = Net().to('cuda')



x1 = torch.randn(1, 32, 11, 18)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
forward() takes 0 positional arguments but 2 were given

jit:
forward() takes 0 positional arguments but 2 were given
'''