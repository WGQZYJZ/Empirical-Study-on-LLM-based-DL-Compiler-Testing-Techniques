'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.resolve_neg\ntorch.resolve_neg(input)\n'
import torch
input = torch.randint(low=0, high=10, size=(3, 3), dtype=torch.long)
output = torch.resolve_neg(input)
print('input data: ', input)
print('output data: ', output)