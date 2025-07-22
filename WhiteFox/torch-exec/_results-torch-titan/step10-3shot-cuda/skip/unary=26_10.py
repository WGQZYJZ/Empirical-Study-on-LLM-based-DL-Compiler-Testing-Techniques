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
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1, output_padding=1)
        self.conv2 = torch.nn.Conv2d(8, 16, kernel_size=3, stride=2, padding=1, output_padding=1)

    def forward(self, x1):
        x1 = self.conv_transpose(x1)
        x1 = self.conv2(x1)
        x1 = (x1 > 0)
        return x1




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]
