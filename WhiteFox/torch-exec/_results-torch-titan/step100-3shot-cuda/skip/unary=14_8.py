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
        self.conv_transpose4 = torch.nn.ConvTranspose2d(1, 1, 1, stride=(1, 2), groups=4, padding=(0, 1), dilation=(1, 1), output_padding=(0, 0))

    def forward(self, x1):
        v1 = self.conv_transpose4(x1)
        v2 = torch.sigmoid(v1)
        v3 = (v1 * v2)
        return v3




func = Model().to('cuda')



x1 = torch.randn(1, 1, 4, 4)


test_inputs = [x1]
