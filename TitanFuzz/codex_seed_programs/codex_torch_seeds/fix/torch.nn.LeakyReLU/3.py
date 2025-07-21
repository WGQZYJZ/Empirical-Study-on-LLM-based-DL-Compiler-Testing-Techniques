'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LeakyReLU\ntorch.nn.LeakyReLU(negative_slope=0.01, inplace=False)\n'
import torch
x = torch.randn(10, 10)
relu = torch.nn.LeakyReLU(negative_slope=0.01, inplace=False)
y = relu(x)
print('x: ', x)
print('y: ', y)