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

    def __init__(self, conv_op, split_op):
        super().__init__()
        convs = []
        split_points = [1, 1]
        for i in range(len(split_points) - 1):
            (convs.append(conv_op), convs.append(split_op))
        self.features = torch.nn.Sequential(convs, torch.nn.Conv2d(3, 3, 3, 1, 1))

    def forward(self, x1):
        v1 = self.features(x1)
        return v1


conv_op = 1
split_op = 1

func = Model(conv_op, split_op).to('cpu')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]
