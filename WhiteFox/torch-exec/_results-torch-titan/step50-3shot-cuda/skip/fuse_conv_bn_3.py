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

    def __init__(self, conv_op):
        super().__init__()
        self.conv = conv_op()
        self.bn = torch.nn.BatchNorm2d(8)

    def forward(self, x):
        y = self.conv(x)
        y = self.bn(self.conv(y))
        return y



conv_op = 1

func = Model(conv_op).to('cuda')



x = torch.randn(1, 8, 16, 16)


test_inputs = [x]
