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
        conv = torch.nn.ConvXd
        bn = torch.nn.BatchNormXd
        self.conv1 = conv(3, 16, kernel_size=(1, 3), padding=(0, 1))
        self.bn1 = bn(16, eps=1e-05)

    def forward(self, x):
        x1 = self.conv1(x)
        x2 = self.bn1(x1)
        return x2




func = Model().to('cuda')



x = torch.randn(1, 3, 4, 8)


test_inputs = [x]
