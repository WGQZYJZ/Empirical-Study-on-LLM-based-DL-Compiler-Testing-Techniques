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
        self.convt2d = torch.nn.ConvTranspose2d(3, 2, 5, padding=8, output_padding=7)

    def forward(self, x1):
        v1 = self.convt2d(x1)
        v2 = torch.sigmoid(v1)
        return v2




func = Model().to('cuda')



x1 = torch.randn(1, 3, 5, 13)


test_inputs = [x1]

# JIT_STATUS
'''
direct:
output padding must be smaller than either stride or dilation, but got output_padding_height: 7 output_padding_width: 7 stride_height: 1 stride_width: 1 dilation_height: 1 dilation_width: 1

jit:

'''