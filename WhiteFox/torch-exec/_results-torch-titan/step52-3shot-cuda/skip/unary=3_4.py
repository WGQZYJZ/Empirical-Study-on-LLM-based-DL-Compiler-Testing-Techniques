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
        self.conv = torch.nn.Conv2d(3, 3, padding=0, stride=2)

    def forward(self, x1):
        v1 = self.conv(x1)
        return v1




func = Model().to('cuda')



x1 = torch.randn(1, 3, 150, 185)


test_inputs = [x1]
