'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.resolve_neg\ntorch.resolve_neg(input)\n'
import torch
input = torch.randn(2, 3)
result = torch.resolve_neg(input)
print(input)
print(result)