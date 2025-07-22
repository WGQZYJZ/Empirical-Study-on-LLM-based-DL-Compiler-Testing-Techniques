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
        self.conv_transpose_4 = torch.nn.ConvTranspose2d(12, 273, 3, stride=(1, 2), padding=1, output_padding=(0, 0), groups=(4, 6), dilation=(4, 4))

    def forward(self, x1):
        v1 = self.conv_transpose_4(x1)
        v2 = torch.sigmoid(v1)
        v3 = v1 * v2
        return v3



func = Model().to('cpu')


x1 = torch.randn(12, 4, 1, 1, 12)

test_inputs = [x1]
