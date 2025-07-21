'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.unbind\ntorch.unbind(input, dim=0)\n'
import torch
input = torch.randn(2, 3, 4)
output = torch.unbind(input, dim=0)
print(output)
print(output[0].shape)
print(output[1].shape)