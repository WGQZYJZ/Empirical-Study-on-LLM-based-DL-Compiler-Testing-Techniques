'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.view_as_complex\ntorch.view_as_complex(input)\n'
import torch
input = torch.randn(4, 2)
output = torch.view_as_complex(input)
print('input', input)
print('output', output)