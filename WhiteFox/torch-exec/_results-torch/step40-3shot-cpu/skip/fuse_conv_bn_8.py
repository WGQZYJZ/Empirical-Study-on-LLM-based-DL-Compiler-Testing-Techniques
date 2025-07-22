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
        self.conv2d = torch.nn.Conv2d(3, 2, stride=1, groups=3)

    def forward(self, x):
        x1 = F.batch_norm(self.conv2d(x), running_mean=torch.zeros(2), running_var=torch.ones(2), weight=torch.ones(2), bias=torch.zeros(2), training=torch.onnx.is_in_onnx_export())
        return x1



func = Model().to('cpu')


x1 = torch.randn(1, 3, 2, 2)

test_inputs = [x1]
