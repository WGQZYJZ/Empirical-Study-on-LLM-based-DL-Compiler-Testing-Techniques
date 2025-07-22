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
    __constants__ = ['other']

    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 224, strides=[2, 2])
        self.other = torch.zeros((224, 3, 3, 3), dtype=torch.float32)

    def forward(self, x2):
        v7 = self.conv(x2)
        return (v7 + self.other)



func = Model().to('cuda')



x2 = torch.randn(1, 3, 64, 64)


test_inputs = [x2]
