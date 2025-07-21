'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.resolve_neg\ntorch.resolve_neg(input)\n'
import torch
input = torch.tensor([(- 1), (- 2), (- 3), (- 4), (- 5), (- 6), (- 7), (- 8), (- 9), (- 10)])
print(torch.resolve_neg(input))