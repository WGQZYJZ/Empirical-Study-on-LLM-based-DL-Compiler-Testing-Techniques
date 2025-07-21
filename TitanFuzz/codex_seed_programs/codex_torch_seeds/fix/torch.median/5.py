'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.median\ntorch.median(input, dim=-1, keepdim=False, *, out=None)\n'
import torch
input_tensor = torch.randn(3, 5)
output_tensor = torch.median(input_tensor, dim=(- 1))
print(output_tensor)