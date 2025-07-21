'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.mv\ntorch.mv(input, vec, *, out=None)\n'
import torch
input_data = torch.randn(4, 3)
vec = torch.randn(3)
output = torch.mv(input_data, vec)
print(output)