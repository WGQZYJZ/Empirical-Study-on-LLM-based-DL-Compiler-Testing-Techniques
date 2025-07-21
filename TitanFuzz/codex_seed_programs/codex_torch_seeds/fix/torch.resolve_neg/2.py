'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.resolve_neg\ntorch.resolve_neg(input)\n'
import torch
input = torch.rand(1, 3, 3)
output = torch.resolve_neg(input)
print(output)