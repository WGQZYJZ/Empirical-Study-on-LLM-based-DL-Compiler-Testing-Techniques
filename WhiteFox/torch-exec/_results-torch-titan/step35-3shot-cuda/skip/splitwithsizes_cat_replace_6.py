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

    def __init__(self, split_sizes):
        super().__init__()
        self.feature0_out_features = split_sizes[0]
        self.feature1_out_features = split_sizes[1]
        self.feature2_out_features = split_sizes[2]
        self.features = torch.nn.ModuleList([torch.nn.Conv2d(3, 32, 3, 1, 1), torch.nn.MaxPool2d(3, 2, 1), torch.nn.Conv2d(32, 32, 3, 1, 1), torch.nn.AvgPool2d(3, 1, 3)])

    def forward(self, v0):
        (s0, s1, s2) = torch.split(v0, [self.feature0_out_features, self.feature1_out_features, self.feature2_out_features], dim=(- 3))
        return (s0, s1, s2)



split_sizes = 1

func = Model(split_sizes).to('cuda')



v0 = torch.randn(1, 3, 64, 64)


test_inputs = [v0]
