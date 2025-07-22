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
        self.conv = torch.nn.Conv2d(4, 3, 3, padding=(1, 1), groups=4)

    def forward(self, x):
        v1 = self.conv(x)
        v2 = (v1 - 5)
        return v2




func = Model().to('cuda')



x = torch.randn(1, 4, 32, 32)


test_inputs = [x]
