'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.corrcoef\ntorch.corrcoef(input)\n'
import torch
input = torch.randn(10, 10)
output = torch.corrcoef(input)
print(output)