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
        self.conv = torch.nn.Conv2d(2, 4, (3, 4), stride=(1, 1), padding=(3, 0), bias=False, groups=2, dilation=2, padding_mode='same')

    def forward(self, x, y):
        v1 = self.conv(x)
        v2 = (v1 - y)
        return v2




func = Model().to('cuda')



x = torch.randn(1, 2, 6, 2)



y = torch.randn(1, 4, 4, 4)


test_inputs = [x, y]
