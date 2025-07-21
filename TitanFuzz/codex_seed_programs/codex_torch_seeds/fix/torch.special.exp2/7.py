'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.exp2\ntorch.special.exp2(input, *, out=None)\n'
import torch
input_data = torch.randn(1, 2, 3)
print(input_data)
output = torch.special.exp2(input_data)
print(output)