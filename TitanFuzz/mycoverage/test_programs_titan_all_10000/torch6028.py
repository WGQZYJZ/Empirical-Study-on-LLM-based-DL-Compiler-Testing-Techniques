import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.Tensor([float('inf'), float('-inf'), float('nan'), 1, 2, 3])
output_data = torch.isinf(input_data)