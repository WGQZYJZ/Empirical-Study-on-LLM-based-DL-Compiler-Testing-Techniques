'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.permute\ntorch.permute(input, dims)\n'
import torch
input = torch.arange(0, 6).view(2, 3)
print(input)
output = torch.permute(input, (1, 0))
print(output)