'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.frac\ntorch.frac(input, *, out=None)\n'
import torch
input_data = torch.rand(4, 4)
print('Input data: ', input_data)
frac_result = torch.frac(input_data)
print('Result: ', frac_result)