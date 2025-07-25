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

class MyModel(nn.Module):

    def __init__(self):
        super().__init__()
        self.conv1 = Conv2d(20, 50, kernel_size=5, padding=2)
        self.conv2 = Conv2d(50, 100, kernel_size=5, padding=2)
        self.conv3 = Conv2d(50, 100, kernel_size=5, padding=2)
        self.conv4 = Conv2d(200, 100, kernel_size=5, padding=2)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = F.max_pool2d(x, 2, 2)
        x = F.relu(self.conv2(x))
        x = F.relu(self.conv3(x))
        x = F.max_pool2d(x, 2, 2)
        x = F.relu(self.conv4(x))
        x = x.view(-1, 100 * 4 * 4)
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x



func = MyModel().to('cpu')



x = torch.randn(1, 20, 100, 100, dtype=torch.float64)

test_inputs = [x]
