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
        self.conv_transpose1 = torch.nn.ConvTranspose2d(2, 3, 12, 2, 13, 0, 15, 30)
        self.conv_transpose2 = torch.nn.ConvTranspose2d(4, 12, 1, 1, 0, 0, 3, 4)

    def forward(self, x1):
        v1 = self.conv_transpose1(x1)
        v2 = v1 + 3
        v3 = torch.clamp(v2, min=0)
        v4 = torch.clamp(v3, max=6)
        v5 = v1 * v4
        v6 = v5 / 6
        return self.conv_transpose2(v6)



func = Model().to('cpu')


x1 = torch.randn(1, 2, 1, 4)

test_inputs = [x1]
