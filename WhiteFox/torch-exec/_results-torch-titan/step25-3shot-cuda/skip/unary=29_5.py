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
        super(Model, self).__init__()
        self.sigmoid = torch.nn.Sigmoid()
        self.conv_transpose = torch.nn.ConvTranspose2d(1, 1, 1, stride=1, padding=1)
        self.act_4 = torch.nn.LeakyReLU()
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x):
        v2 = self.conv_transpose(x)
        v3 = torch.clamp_min(v2, self.min_value)
        v4 = torch.clamp_max(v3, self.max_value)
        return v4




func = Model().to('cuda')



x = torch.randn(1, 1, 13, 13)


test_inputs = [x]
