'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.transpose\ntorch.transpose(input, dim0, dim1)\n'
import torch
input = torch.randn(1, 2, 3, 4)
output = torch.transpose(input, 1, 2)
print(output.size())