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
        self.conv1 = torch.nn.Conv(3, 16, 32)
        self.conv2 = torch.nn.Conv(16, 32, 64)
        self.conv3 = torch.nn.Conv(32, 64, 128)
        self.conv4 = torch.nn.Conv(64, 9, 256)

    def forward(self, image):
        x1 = self.conv1(image)
        x2 = F.relu(x1)
        x3 = self.conv2(x2)
        x4 = F.relu(x3)
        x5 = self.conv3(x4)
        x6 = F.relu(x5)
        x7 = self.conv4(x6)
        return x7



func = Model().to('cpu')


image = torch.randn(1, 3, 64, 64)

test_inputs = [image]
