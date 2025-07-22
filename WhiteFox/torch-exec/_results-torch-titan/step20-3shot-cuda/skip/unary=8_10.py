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
        self.conv1 = torch.nn.Conv2d(1, 1, kernel_size=(1, 30), stride=(1, 10), padding=(0, 15), dilation=(1, 1))
        self.relu = torch.nn.ReLU(inplace)

    def forward(self, input):
        x = self.conv1(input)
        x = self.relu(x)
        x = x.permute(0, 2, 3, 1)
        output = nn.functional.adaptive_avg_pool2d(x, (1, 1)).reshape(x.shape[0], (- 1))
        return output




func = Model().to('cuda')



x1 = torch.randn(1, 1, 6, 15)


test_inputs = [x1]
