'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isnan\ntorch.isnan(input)\n'
import torch
A = torch.randn(2, 3)
print(A)
print(torch.isnan(A))