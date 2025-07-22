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
        self.conv = torch.nn.Conv2d(2, 2, 1, padding=0, bias=False)
        self.add = torch.nn.functional.add

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.add(x1, v1)
        return v2




func = Model().to('cuda')



x1 = torch.randn(1, 2, 64, 64)


test_inputs = [x1]
