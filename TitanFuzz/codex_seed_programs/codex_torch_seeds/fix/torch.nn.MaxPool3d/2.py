'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.MaxPool3d\ntorch.nn.MaxPool3d(kernel_size, stride=None, padding=0, dilation=1, return_indices=False, ceil_mode=False)\n'
import torch
from torch.autograd import Variable
import torch
in_channels = 1
input_size = (1, in_channels, 4, 4, 4)
input = Variable(torch.randn(input_size))
pool = torch.nn.MaxPool3d(kernel_size=2)
output = pool(input)
print(output.size())