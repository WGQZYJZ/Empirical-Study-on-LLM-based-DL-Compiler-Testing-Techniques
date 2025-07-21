'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.MaxUnpool2d\ntorch.nn.MaxUnpool2d(kernel_size, stride=None, padding=0)\n'
import torch
from torch.autograd import Variable
input_data = Variable(torch.randn(1, 1, 4, 4))
pool = torch.nn.MaxPool2d(2, stride=2, return_indices=True)
unpool = torch.nn.MaxUnpool2d(2, stride=2)
(output, indices) = pool(input_data)
unpooled_output = unpool(output, indices)
print(input_data)
print(output)
print(unpooled_output)