'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.is_complex\ntorch.is_complex(input)\n'
import torch
input = torch.tensor([1, 2, 3, 4, 5])
output = torch.is_complex(input)
print('input: ', input)
print('output:', output)