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

    def __init__(self, negative_slope, size_average=True, reduce=True):
        super().__init__()
        self.conv_t1 = torch.nn.ConvTranspose2d(63, 112, 3, stride=1, bias=False, padding=1)
        self.conv_t2 = torch.nn.ConvTranspose2d(112, 63, 3, stride=2, bias=False, padding=1, dilation=2)
        self.negative_slope = negative_slope


negative_slope = 1

func = Model(negative_slope).to('cpu')

input_tensor = torch.randn(1, 1, 1)

test_inputs = [input_tensor]

# JIT_FAIL
'''
direct:
Module [Model] is missing the required "forward" function

jit:
Module [Model] is missing the required "forward" function
'''