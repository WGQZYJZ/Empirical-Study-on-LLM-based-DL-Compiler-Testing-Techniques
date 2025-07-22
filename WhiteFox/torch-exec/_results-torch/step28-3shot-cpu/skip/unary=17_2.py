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
        self.conv = torch.nn.ConvTranspose2d(1, 1, 3, padding_mode='replicate')

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.relu(v1)
        return v2



func = Model().to('cpu')


x1 = torch.randn(1, 1, 2, 5)

test_inputs = [x1]
