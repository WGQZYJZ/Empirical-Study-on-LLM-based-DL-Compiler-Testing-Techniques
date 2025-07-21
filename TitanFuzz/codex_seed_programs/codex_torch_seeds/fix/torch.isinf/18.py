'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isinf\ntorch.isinf(input)\n'
import torch
input = torch.randn(2, 3, 4, 5)
output = torch.isinf(input)
print(output)