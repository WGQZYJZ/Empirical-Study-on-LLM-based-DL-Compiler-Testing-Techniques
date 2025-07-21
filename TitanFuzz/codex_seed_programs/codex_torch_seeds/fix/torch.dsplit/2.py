'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.dsplit\ntorch.dsplit(input, indices_or_sections)\n'
import torch
input = torch.randn(2, 3, 4, 5)
torch.dsplit(input, 2)
torch.dsplit(input, [1, 2])
torch.dsplit(input, [2, 3])
print('Done!')