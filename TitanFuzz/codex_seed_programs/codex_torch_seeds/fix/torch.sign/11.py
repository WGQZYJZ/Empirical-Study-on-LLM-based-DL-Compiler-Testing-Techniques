'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sign\ntorch.sign(input, *, out=None)\n'
import torch
input_tensor = torch.randn(4, 4)
print(input_tensor)
output_tensor = torch.sign(input_tensor)
print(output_tensor)