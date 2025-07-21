'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.resolve_neg\ntorch.resolve_neg(input)\n'
import torch
x = torch.randn(3, 3)
print(x)
y = torch.resolve_neg(x)
print(y)