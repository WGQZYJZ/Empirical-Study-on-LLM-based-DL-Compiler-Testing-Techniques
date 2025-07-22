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
        self.conv_t_2 = torch.nn.ConvTranspose2d(8, 7, kernel_size=7, stride=(5, 4), groups=2, dilation=(7, 1))

    def forward(self, x1):
        v1 = self.conv_t_2(x1)
        v2 = torch.sigmoid(v1)
        return v2




func = Model().to('cuda')



x1 = torch.randn(3, 8, 777, 777)


test_inputs = [x1]
