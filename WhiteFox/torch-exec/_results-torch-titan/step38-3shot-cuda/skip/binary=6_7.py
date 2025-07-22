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
        for _ in _____:
            self.__i__ = torch.nn.Linear(__in_channels__, __out_channels__, bias=False)

    def forward(self, x1, x2):
        x3 = ___.___
        x4 = self.___(_, _, bias=False)
        x5 = (x3 - x4)
        return x5



func = Model().to('cuda')



x1 = torch.randn(10, 3)



x2 = torch.randn(3, 5)


test_inputs = [x1, x2]
