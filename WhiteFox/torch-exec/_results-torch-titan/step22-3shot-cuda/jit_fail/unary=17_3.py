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

    def forward(self, x1):
        v1 = F.conv_transpose3d(x1, torch.randn(3, 3, 3, 3, 3), bias=None, stride=2, padding=0, dilation=2)
        return v1




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 4, 4)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Input type (torch.cuda.FloatTensor) and weight type (torch.FloatTensor) should be the same

jit:
Input type (torch.cuda.FloatTensor) and weight type (torch.FloatTensor) should be the same
'''