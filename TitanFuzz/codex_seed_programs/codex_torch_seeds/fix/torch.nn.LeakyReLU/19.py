'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LeakyReLU\ntorch.nn.LeakyReLU(negative_slope=0.01, inplace=False)\n'
import torch
from torch.autograd import Variable
input_data = Variable(torch.randn(5, 3))
leaky_relu = torch.nn.LeakyReLU(negative_slope=0.01, inplace=False)
output_data = leaky_relu(input_data)
print('input_data:\n', input_data)
print('output_data:\n', output_data)
print('input_data.size():\n', input_data.size())
print('output_data.size():\n', output_data.size())