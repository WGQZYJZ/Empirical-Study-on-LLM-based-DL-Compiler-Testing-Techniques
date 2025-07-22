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
        self.conv0 = torch.nn.Conv2d(4, 8, 3)
        self.conv1 = torch.nn.Conv2d(8, 8, 1)
        self.conv1[(- 1)].bias = torch.nn.Parameter(torch.ones(8))

    def forward(self, input):
        x = self.conv0(input)
        return (self.conv1(x) + torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0, 5.0, 6.0, 7.0])[None, :, None, None])




func = Model().to('cuda')



x3 = torch.randn(2, 4, 8, 8)


test_inputs = [x3]
