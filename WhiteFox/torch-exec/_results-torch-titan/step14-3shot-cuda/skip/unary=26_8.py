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
        self.conv_t_3 = torch.nn.ConvTranspose2d(3, 10, (1, 4, 1, 5), groups=3, padding=(1, 1, 1, 4), bias=False)
        self.relu_1 = torch.nn.ReLU()

    def forward(self, x):
        v1 = self.conv_t_3(x)
        v2 = (v1 > 0)
        v3 = (v1 * 2)
        v4 = torch.where(v2, v1, v3)
        v5 = self.relu_1(v4)
        return v5




func = Model().to('cuda')




x = torch.randn(16, 3, 16, 19, 13, 20).to(torch.float32)




y = torch.randn(16, 10, 16, 19, 13, 20).to(torch.float32)


test_inputs = [x, y]
