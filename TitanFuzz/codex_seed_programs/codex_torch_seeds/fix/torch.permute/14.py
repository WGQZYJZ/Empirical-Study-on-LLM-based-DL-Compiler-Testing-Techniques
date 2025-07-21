'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.permute\ntorch.permute(input, dims)\n'
import torch
input = torch.randn(2, 3, 5)
print(input)
print(input.shape)
print('\n')
output = torch.permute(input, (1, 0, 2))
print(output)
print(output.shape)