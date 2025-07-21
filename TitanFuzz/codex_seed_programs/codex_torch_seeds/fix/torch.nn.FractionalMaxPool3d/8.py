'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.FractionalMaxPool3d\ntorch.nn.FractionalMaxPool3d(kernel_size, output_size=None, output_ratio=None, return_indices=False, _random_samples=None)\n'
import torch
from torch.autograd import Variable
import torch.nn as nn
import torch
input_data = Variable(torch.randn(20, 16, 50, 32, 45))
pool = nn.FractionalMaxPool3d(3, output_size=[13, 11, 9])
output = pool(input_data)
print(output.shape)