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
        self.features1 = torch.nn.Conv2d(1, 2, 3, 1, groups=2)
        self.features2 = torch.nn.Conv2d(4, 8, 3, 1)
        self.features3 = torch.nn.Conv2d(3, 3, 3, 1)

    def forward(self, v1):
        split_tensors1 = torch.split(self.features1(v1)[0], [1, 1, 1], dim=1)
        split_tensors2 = torch.split(self.features2(v1)[:, 1], [1, 1, 1, 1, 1, 1, 1], dim=1)
        split_tensors3 = torch.split(self.features3(v1)[:, :, 1], [1, 1], dim=2)
        return (self.features3(v1), torch.cat(((split_tensors1 + split_tensors2) + split_tensors3), dim=1))




func = Model().to('cuda')



x1 = torch.randn(1, 1, 64, 64)


test_inputs = [x1]
