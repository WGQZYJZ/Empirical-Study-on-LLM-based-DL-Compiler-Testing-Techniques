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

    def __init__(self, min_value=4, max_value=9):
        super().__init__()
        self.padding = collections.OrderedDict()
        self.padding['count_include_pad'] = 0
        self.padding['mode'] = 'circular'
        self.conv_transpose = torch.nn.ConvTranspose1d(1, 1, 3, stride=1, dilation=2, padding_dict=self.padding)
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = torch.clamp_min(v1, self.min_value)
        v3 = torch.clamp_max(v2, self.max_value)
        return v3




func = Model().to('cuda')



x1 = torch.randn(1, 1, 64, 64)


test_inputs = [x1]
