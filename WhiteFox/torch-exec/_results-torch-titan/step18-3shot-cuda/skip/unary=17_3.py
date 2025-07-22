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
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 8, 3, groups=2)

    def forward(self, x_in):
        x_in = x_in.permute(0, 3, 2, 1)
        l1 = torch.relu(self.conv_transpose(x_in))
        return l1




func = Model().to('cuda')



x_in = torch.randn(1, 128, 128, 3)


test_inputs = [x_in]
