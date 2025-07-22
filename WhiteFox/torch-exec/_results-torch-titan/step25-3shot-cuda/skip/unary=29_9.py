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
        self.sigmoid = torch.nn.Sigmoid()
        self.conv_transpose = torch.nn.ConvTranspose2d(4, 4, 1, stride=1, padding=0)
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x4):
        v5 = self.conv_transpose(x4)
        v6 = torch.clamp_min(v5, self.min_value)
        v7 = torch.clamp_max(v6, self.max_value)
        return v7




func = Model().to('cuda')



x4 = torch.randn(1, 4, 124, 124)


test_inputs = [x4]
