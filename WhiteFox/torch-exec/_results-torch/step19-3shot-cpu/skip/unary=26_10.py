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

class Model:

    def __init__(self, negative_slope):
        self.conv_t = torch.nn.ConvTranspose2d(19, 64, 1, stride=1, padding=0)
        self.negative_slope = negative_slope

    def forward(self, x2):
        v1 = self.conv_t(x2)
        v2 = v1 > 0
        v3 = v1 * self.negative_slope
        v4 = torch.where(v2, v1, v3)
        return v4


negative_slope = -150

func = Model(negative_slope).to('cpu')


x2 = torch.randn(8, 19, 4, 4)

test_inputs = [x2]
