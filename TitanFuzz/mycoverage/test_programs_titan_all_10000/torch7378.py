import torch
from torch import nn
from torch.autograd import Variable
batch_size = 3
num_channels = 1
sequence_length = 5
input_data = torch.randn(batch_size, num_channels, sequence_length)
output_data = torch.nn.functional.max_pool1d(input_data, kernel_size=2, stride=1, padding=0)