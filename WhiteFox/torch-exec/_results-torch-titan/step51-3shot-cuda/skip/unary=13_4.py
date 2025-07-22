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
        self.conv = nn1
        self.sigmoid = nn2
        self.linear = nn3

    def forward(self, x1, x2):
        v1 = self.conv(x1)
        v2 = self.sigmoid(v1)
        v3 = (v1 * v2)
        v4 = self.linear(x2)
        v5 = self.sigmoid(v4)
        v6 = (v4 * v5)
        return torch.cat((v3, v6), 0)



func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)



x2 = torch.randn(6, 3, 64, 64)


test_inputs = [x1, x2]
