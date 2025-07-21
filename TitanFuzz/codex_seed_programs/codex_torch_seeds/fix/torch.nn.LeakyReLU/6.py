'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LeakyReLU\ntorch.nn.LeakyReLU(negative_slope=0.01, inplace=False)\n'
import torch
import torch.nn as nn
input = torch.randn(1, 3)
leaky_relu = nn.LeakyReLU(0.01)
output = leaky_relu(input)
print(output)
if torch.all(output.eq(torch.max(input, torch.zeros_like(input)))):
    print('The result is correct!')
else:
    print('The result is wrong!')