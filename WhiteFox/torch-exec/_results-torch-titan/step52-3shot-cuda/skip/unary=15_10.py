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
        self.conv1 = torch.nn.Conv2d(3, 64, kernel_size=7, stride=2, padding=3, groups=32)
        self.conv2 = torch.nn.Conv2d(16, 128, kernel_size=1, stride=1, padding=0)
        self.conv3 = torch.nn.Conv2d(32, 16, kernel_size=1, stride=1, padding=0)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = torch.relu(v1)
        v2_group2 = v2[:, 0:16, :, :]
        v2_group1 = v2[:, 16:32, :, :]
        v3 = self.conv2(v2_group2)
        v4 = self.conv3(v2_group1)
        return (v3 + v4)




func = Model().to('cuda')



x1 = torch.randn(4, 3, 224, 224)


test_inputs = [x1]
