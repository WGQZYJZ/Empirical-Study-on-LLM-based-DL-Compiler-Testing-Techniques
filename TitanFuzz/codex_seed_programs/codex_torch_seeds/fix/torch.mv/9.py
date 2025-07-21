'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.mv\ntorch.mv(input, vec, *, out=None)\n'
import torch
input_data = torch.randn(2, 3)
vec = torch.tensor([1, 0, (- 1)], dtype=torch.float)
output = torch.mv(input_data, vec)
print('input_data:', input_data)
print('vec:', vec)
print('output:', output)