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
        self.conv_t1 = torch.nn.ConvTranspose2d(in_channels=3, out_channels=1, kernel_size=(1, 1), groups=3, bias=False)
        self.conv_t2 = torch.nn.ConvTranspose2d(in_channels=1, out_channels=3, kernel_size=(3, 3), bias=True)

    def forward(self, x1):
        v1 = self.conv_t1(x1)
        v2 = self.conv_t2(v1)
        return v2




func = Model().to('cuda')



x1 = torch.FloatTensor(6, 3, 7, 7)


test_inputs = [x1]
