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
        self.block0 = torch.nn.Sequential(torch.nn.ConvTranspose2d(3, 16, 2, padding=1, stride=2), torch.nn.ReLU(inplace=False), torch.nn.MaxPool2d(kernel_size=3, ceil_mode=False, padding=2, dilations=1, stride=1))

    def forward(self, x):
        v = self.block0(x)
        return v




func = Model().to('cuda')



x = torch.randn(1, 3, 16, 16)


test_inputs = [x]
