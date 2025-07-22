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
        self.features = torch.nn.Sequential(torch.nn.Conv2d(3, 32, 3, 3, 2), torch.nn.AdaptiveAvgPool2d((1, 30)), torch.nn.ReLU(inplace=True), torch.nn.Linear(30, 8))
        self.split = torch.nn.Sequential(torch.nn.QuantizePermute2d(3), torch.nn.MaxPool2d(7, 5, 1, 2))

    def forward(self, v1):
        split_tensors = torch.split(v1, [1, 1, 1], dim=1)
        concatenated_tensor = torch.cat(split_tensors, dim=1)
        return (concatenated_tensor, torch.split(v1, [1, 1, 1], dim=1))



func = Model().to('cpu')


x1 = torch.randn(16, 3, 10, 6)

test_inputs = [x1]
