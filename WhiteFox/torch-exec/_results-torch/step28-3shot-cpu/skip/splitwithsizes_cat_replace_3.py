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
        self.features = torch.nn.ModuleDict(OrderedDict([('conv0', torch.nn.Conv2d(3, 32, 3, 1, 2)), ('conv1', torch.nn.Conv2d(32, 32, 3, 2, 3)), ('conv2', torch.nn.Conv2d(32, 32, 3, 1, 2))]))
        self.conv_last = torch.nn.Conv2d(64, 32, 7, 7, 7)

    def forward(self, v1):
        split_tensors = torch.split(v1, [1, 1, 1], dim=1)
        concatenated_tensor = torch.cat(split_tensors, dim=1)
        last_tensor = self.features(concatenated_tensor)
        last_tensor = self.conv_last(last_tensor)
        return (concatenated_tensor, last_tensor)



func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]
