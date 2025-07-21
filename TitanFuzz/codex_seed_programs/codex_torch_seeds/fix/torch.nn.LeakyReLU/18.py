'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LeakyReLU\ntorch.nn.LeakyReLU(negative_slope=0.01, inplace=False)\n'
import torch
import torch.nn as nn
input_data = torch.randn(5, 3)
print(input_data)
leaky_relu = nn.LeakyReLU(negative_slope=0.01, inplace=False)
output_data = leaky_relu(input_data)
print(output_data)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ReLU6\ntorch.nn.ReLU6(inplace=False)\n'
import torch
import torch.nn as nn
input_data = torch.randn(5, 3)
print(input_data)
relu6 = nn.ReLU6(inplace=False)
output_data = relu6(input_data)
print(output_data)