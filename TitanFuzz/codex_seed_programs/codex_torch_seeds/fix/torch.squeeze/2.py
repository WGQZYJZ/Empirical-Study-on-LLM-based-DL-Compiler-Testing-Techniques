'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.squeeze\ntorch.squeeze(input, dim=None, *, out=None)\n'
import torch
input = torch.randn(1, 1, 1, 3, 1, 1)
print(input.shape)
output = torch.squeeze(input)
print(output.shape)
output = torch.squeeze(input, dim=0)
print(output.shape)
output = torch.squeeze(input, dim=2)
print(output.shape)
output = torch.squeeze(input, dim=4)
print(output.shape)
output = torch.squeeze(input, dim=1)
print(output.shape)