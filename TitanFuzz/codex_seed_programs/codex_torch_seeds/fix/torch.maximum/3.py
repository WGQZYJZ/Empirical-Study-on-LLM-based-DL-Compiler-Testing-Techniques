'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.maximum\ntorch.maximum(input, other, *, out=None)\n'
import torch
input_tensor = torch.rand(3, 3)
other_tensor = torch.rand(3, 3)
max_tensor = torch.maximum(input_tensor, other_tensor)
print(max_tensor)