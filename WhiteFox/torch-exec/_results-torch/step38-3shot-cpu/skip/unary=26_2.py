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
        self.conv_t = torch.nn.ConvTranspose2d(4, 32, 5, padding=3, weight_norm=True)

    def forward(self, x):
        w1 = self.conv_t(x)
        w2 = w1 > 0
        w3 = w1 * -0.751
        w4 = torch.where(w2, w1, w3)
        return w4



func = Model().to('cpu')


x = torch.randn(5, 4, 6, 18)

test_inputs = [x]
