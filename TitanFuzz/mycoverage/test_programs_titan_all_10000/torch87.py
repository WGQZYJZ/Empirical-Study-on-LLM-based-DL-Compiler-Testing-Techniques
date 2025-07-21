import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.arange(0, 27).view(1, 1, 3, 3, 3)
output = torch.nn.functional.avg_pool3d(input_data, kernel_size=3, stride=1, padding=0)