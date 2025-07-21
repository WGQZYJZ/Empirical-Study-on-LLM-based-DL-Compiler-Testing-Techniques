'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.MaxPool3d\ntorch.nn.MaxPool3d(kernel_size, stride=None, padding=0, dilation=1, return_indices=False, ceil_mode=False)\n'
import torch
from torch.autograd import Variable
input_data = Variable(torch.randn(20, 16, 50, 44, 44))
max_pooling_layer = torch.nn.MaxPool3d(kernel_size=2, stride=2, padding=0)
output = max_pooling_layer(input_data)
print('input size: {}\noutput size: {}'.format(input_data.size(), output.size()))