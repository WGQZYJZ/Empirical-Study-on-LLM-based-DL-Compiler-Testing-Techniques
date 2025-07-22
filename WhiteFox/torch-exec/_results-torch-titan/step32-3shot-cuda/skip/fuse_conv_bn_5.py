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
        self.conv = torch.nn.Conv2d(None, None, 3)
        self.bn = torch.nn.BatchNorm2d(None)

    def forward(self, x):
        x1 = self.conv1(x)
        y2 = self.bn(x1)
        return y2




func = Model().to('cuda')



x1 = torch.randn(1, 3, 3, 3)


test_inputs = [x1]
