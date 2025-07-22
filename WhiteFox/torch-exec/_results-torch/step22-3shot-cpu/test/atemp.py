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

    def forward(self, x):
        x1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)(x)
        z = torch.add(x1, 3)
        w = torch.clamp(z, min=0, max=6)
        y = torch.div(w, 6)
        return y



func = Model().to('cpu')


x = torch.randn(1, 3, 64, 64)

test_inputs = [x]
