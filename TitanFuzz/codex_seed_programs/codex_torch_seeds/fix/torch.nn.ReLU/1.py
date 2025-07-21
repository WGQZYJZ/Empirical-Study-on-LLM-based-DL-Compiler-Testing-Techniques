'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ReLU\ntorch.nn.ReLU(inplace=False)\n'
import torch
import torch
input = torch.randn(1, 1, 2, 2)
print(input)
output = torch.nn.ReLU(inplace=False)(input)
print(output)