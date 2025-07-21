'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isnan\ntorch.isnan(input)\n'
import torch
input = torch.randn(4, 4)
input[0][0] = float('nan')
input[1][1] = float('nan')
print(input)
print(torch.isnan(input))