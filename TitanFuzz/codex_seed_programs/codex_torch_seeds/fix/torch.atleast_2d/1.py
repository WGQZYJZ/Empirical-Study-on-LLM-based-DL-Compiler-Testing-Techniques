'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.atleast_2d\ntorch.atleast_2d(*tensors)\n'
import torch
import torch
input_tensor = torch.randn(3, 1, 4)
print(input_tensor)
output_tensor = torch.atleast_2d(input_tensor)
print(output_tensor)