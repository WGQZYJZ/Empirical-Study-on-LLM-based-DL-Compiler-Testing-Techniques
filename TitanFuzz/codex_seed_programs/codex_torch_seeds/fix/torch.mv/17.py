'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.mv\ntorch.mv(input, vec, *, out=None)\n'
import torch
input_data = torch.randn(10, 10)
vec = torch.randn(10)
print(torch.mv(input_data, vec))