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
        dilation_rate = 0
        if (dilation_rate != 0):
            p = math.ceil((((kernel_size + ((dilation_rate - 1) * (kernel_size - 1))) - 1) / 2))
        padding2 = (max(0, (((n + (2 * p)) - k) - ((k - 1) * (d - 1)))) / 2)
        padding_height = padding2
        if (padding_height > 0):
            padding_height = math.floor(padding_height)
        else:
            padding_height = math.ceil(padding_height)
        v = torch.nn.Conv2d(in_channels=3, out_channels=16, kernel_size=(3, 3), stride=s, padding=padding, dilation=dilation, groups=1, bias=False)

    def forward(self, x1):
        v1 = self.v(x1)
        v2 = torch.sigmoid(v1)
        return (v1 * v2)




func = Model().to('cuda')

x1 = 1

test_inputs = [x1]
