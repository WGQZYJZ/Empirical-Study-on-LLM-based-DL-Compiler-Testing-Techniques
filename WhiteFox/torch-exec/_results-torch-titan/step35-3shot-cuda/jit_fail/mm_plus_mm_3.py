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

    def forward(self):
        m1 = torch.nn.Conv2d(in_channels=1, out_channels=1, kernel_size=(2, 2), stride=1, padding=1)
        m2 = torch.nn.Conv2d(in_channels=3, out_channels=1, kernel_size=(2, 2), stride=1, padding=1)
        m3 = torch.nn.Conv2d(in_channels=2, out_channels=1, kernel_size=(3, 3), stride=1, padding=0)
        m4 = torch.nn.Conv2d(in_channels=1, out_channels=1, kernel_size=(2, 2), stride=1, padding=1)
        m5 = torch.nn.Conv2d(in_channels=3, out_channels=1, kernel_size=(1, 1), stride=1, padding=2)
        m6 = torch.nn.Conv2d(in_channels=3, out_channels=1, kernel_size=(2, 2), stride=1, padding=1)
        m7 = torch.nn.Conv2d(in_channels=1, out_channels=1, kernel_size=(1, 1), stride=1, padding=2)
        m8 = torch.nn.Conv2d(in_channels=2, out_channels=1, kernel_size=(1, 1), stride=1, padding=2)
        return 0




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