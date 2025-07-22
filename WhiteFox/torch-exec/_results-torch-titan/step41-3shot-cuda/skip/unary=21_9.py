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



class ModelTanh(nn.Module):

    def __init__(self):
        super(ModelTanh, self).__init__()
        self.conv = nn.Conv2d(1, 1, 11, border_mode=0, dilation=2, groups=1, bias=False, stride=1)

    def forward(self, x):
        y = self.conv(x)
        z = torch.tanh(y)
        return z




func = ModelTanh().to('cuda')



x = torch.rand(2, 1, 256, 128)


test_inputs = [x]
