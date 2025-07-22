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
        self.conv = torch.nn.Conv2d(27, 48, (5, 1), stride=1, padding=1, groups=2)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.nn.Sigmoid()(v1)
        v3 = (v1 * v2)
        return v3




func = Model().to('cuda')



x1 = torch.randn(1, 27, 40, 2)


test_inputs = [x1]
