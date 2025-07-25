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
        torch.manual_seed(1)
        self.conv1 = torch.nn.Conv2d(3, 5, 1)
        torch.manual_seed(1)
        self.bn1 = torch.nn.BatchNorm2d(5)
        torch.manual_seed(1)
        self.bn2 = torch.nn.BatchNorm2d(5)
        torch.manual_seed(1)
        self.conv2 = torch.nn.Conv2d(8, 5, 2, groups=2, padding=3)
        torch.manual_seed(1)
        self.bn3 = torch.nn.BatchNorm2d(5)

    def forward(self, x1):
        x1 = self.conv1(x1)
        x1 = self.bn1(x1) + self.bn2(x1)
        x1 = torch.nn.functional.relu6(x1)
        x1 = self.conv2(x1)
        x1 = self.bn3(x1)
        return x1



func = Model().to('cpu')


x1 = torch.randn(1, 3, 10, 11)

test_inputs = [x1]
