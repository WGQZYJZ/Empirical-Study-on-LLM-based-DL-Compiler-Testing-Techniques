'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.RReLU\ntorch.nn.RReLU(lower=0.125, upper=0.3333333333333333, inplace=False)\n'
import torch
x = torch.randn(1, requires_grad=True)
relu = torch.nn.RReLU(lower=0.125, upper=0.3333333333333333, inplace=False)
print(relu(x))