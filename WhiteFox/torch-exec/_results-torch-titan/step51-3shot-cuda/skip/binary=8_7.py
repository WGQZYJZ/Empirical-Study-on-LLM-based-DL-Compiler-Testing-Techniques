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
        self.conv1 = torch.nn.Conv2d(3, 8, 3, stride=3, padding=3, groups=3, bias=True)
        self.bn1 = torch.nn.BatchNorm2d(8)

    def forward(self, x):
        v1 = self.conv1(x)
        v2 = self.bn1(v1)
        return v2




func = Model().to('cuda')



x = torch.randn(1, 3, 32, 32)


test_inputs = [x]
