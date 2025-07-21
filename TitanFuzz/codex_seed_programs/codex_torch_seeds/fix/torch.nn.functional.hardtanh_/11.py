'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.hardtanh_\ntorch.nn.functional.hardtanh_(input, min_val=-1., max_val=1.)\n'
import torch
input = torch.randn(5, 5)
print('Input: \n', input)
output = torch.nn.functional.hardtanh_(input, min_val=(- 1.0), max_val=1.0)
print('Output: \n', output)