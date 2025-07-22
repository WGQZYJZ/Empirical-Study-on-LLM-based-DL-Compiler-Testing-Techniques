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
        self.conv_t = torch.nn.ConvTranspose2d(10, 18, 1, stride=2, bias=False, groups=8)

    def forward(self, x0):
        v2 = self.conv_t(x0)
        v3 = (v2 > 0)
        v4 = (v2 * (- 0.29))
        v5 = torch.where(v3, v2, v4)
        return v5.neg()




func = Model().to('cuda')



x0 = torch.randn(2, 8, 3, 3)


test_inputs = [x0]
