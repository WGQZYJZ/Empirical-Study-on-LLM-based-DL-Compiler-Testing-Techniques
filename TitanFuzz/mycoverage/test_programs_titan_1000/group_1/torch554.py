import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.arange(1, 17, dtype=torch.float32).view(1, 1, 4, 4)
output_size = (3, 3)
output = torch.nn.functional.adaptive_avg_pool2d(input_data, output_size)