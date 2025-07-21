'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.dsplit\ntorch.dsplit(input, indices_or_sections)\n'
import torch
input = torch.randn(3, 8, 4)
print(input)
print(torch.dsplit(input, 2))
print(torch.dsplit(input, [2, 4]))