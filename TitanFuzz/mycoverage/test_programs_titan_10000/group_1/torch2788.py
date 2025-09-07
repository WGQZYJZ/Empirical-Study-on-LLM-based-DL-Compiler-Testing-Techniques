import torch
from torch import nn
from torch.autograd import Variable

input_data = torch.tensor([4.0])
output_data = torch.rsqrt(input_data)