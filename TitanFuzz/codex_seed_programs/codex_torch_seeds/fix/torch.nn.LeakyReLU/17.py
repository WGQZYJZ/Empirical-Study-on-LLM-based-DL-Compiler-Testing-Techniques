'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LeakyReLU\ntorch.nn.LeakyReLU(negative_slope=0.01, inplace=False)\n'
import torch
from torch.autograd import Variable
input_data = Variable(torch.randn(5, 3))
print(input_data)
leaky_relu = torch.nn.LeakyReLU(0.2)
output_data = leaky_relu(input_data)
print(output_data)