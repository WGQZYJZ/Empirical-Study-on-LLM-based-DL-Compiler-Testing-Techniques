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
        self.a = torch.nn.ConvTranspose2d(3, 3, 2)
        self.b = torch.nn.Batchnorm2d(3, affine=True)
        self.c = torch.nn.Conv2d(3, 3, 2)

    def forward(self, x):
        x = self.a(x)
        x = self.b(x)
        y = self.c(x)
        return y



func = Model().to('cpu')


x = torch.randn(3, 3, 14, 14)

test_inputs = [x]
