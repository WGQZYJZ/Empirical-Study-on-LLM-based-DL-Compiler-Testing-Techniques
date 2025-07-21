'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.resolve_neg\ntorch.resolve_neg(input)\n'
import torch
x = torch.tensor([[0, (- 1), (- 2), (- 3)], [1, 2, 3, 4]])
print(x)
print(torch.resolve_neg(x))