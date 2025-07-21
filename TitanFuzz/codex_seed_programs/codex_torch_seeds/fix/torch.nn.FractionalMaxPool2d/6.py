'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.FractionalMaxPool2d\ntorch.nn.FractionalMaxPool2d(kernel_size, output_size=None, output_ratio=None, return_indices=False, _random_samples=None)\n'
import torch
import torch.nn as nn
from torch.autograd import Variable
dtype = torch.FloatTensor
input_data = Variable(torch.randn(20, 16, 50, 32).type(dtype), requires_grad=False)
max_pool = nn.FractionalMaxPool2d(kernel_size=(3, 3), output_size=(5, 5))
output = max_pool(input_data)
print(output.size())