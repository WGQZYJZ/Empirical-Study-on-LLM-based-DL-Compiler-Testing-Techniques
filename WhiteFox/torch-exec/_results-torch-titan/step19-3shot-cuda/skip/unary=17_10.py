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
        self.conv = torch.nn.ConvTranspose2d(3, 16, 3, padding=1, stride=2)
        self.linear = torch.nn.Linear((205440 / 4), 8)

    def forward(self, x1):
        v1 = self.conv(x1)
        t1 = v1.reshape((v1.shape[0], (- 1)))
        v2 = self.linear(t1)
        return v2




func = Model().to('cuda')



x1 = torch.randn(1, 3, 16, 16)


test_inputs = [x1]
