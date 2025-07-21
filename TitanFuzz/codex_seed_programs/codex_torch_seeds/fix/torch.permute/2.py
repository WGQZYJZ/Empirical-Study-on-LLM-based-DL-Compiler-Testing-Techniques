'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.permute\ntorch.permute(input, dims)\n'
import torch
input = torch.randn(2, 3, 5)
print(input)
dims = [1, 2, 0]
output = torch.permute(input, dims)
print(output)