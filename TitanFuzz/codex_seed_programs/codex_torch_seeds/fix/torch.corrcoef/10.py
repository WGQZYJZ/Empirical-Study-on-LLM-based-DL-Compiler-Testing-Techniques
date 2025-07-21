'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.corrcoef\ntorch.corrcoef(input)\n'
import torch
input = torch.randn(5, 5)
print(torch.corrcoef(input))