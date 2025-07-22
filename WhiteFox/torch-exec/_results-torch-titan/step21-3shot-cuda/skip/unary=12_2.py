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
        self.conv1 = torch.nn.Conv2d(in_channels=3, out_channels=8, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
        self.conv2 = torch.nn.Conv2d(in_channels=32, out_channels=64, kernel_size=(1, 1), stride=(1, 1), padding=(0, 0))
        self.concat = torch.cat((torch.reshape(self.conv1, ((- 1), 32, 1)), torch.reshape(self.conv2, ((- 1), 64, 1))), dim=2)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        v3 = torch.reshape(v2, ((- 1), (32 * 64), 1))
        return v3




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]
