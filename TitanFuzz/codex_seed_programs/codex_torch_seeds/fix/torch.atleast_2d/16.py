'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.atleast_2d\ntorch.atleast_2d(*tensors)\n'
import torch
input_data = torch.randn(1, 2, 3, 4)
output_data = torch.atleast_2d(input_data)
print(output_data)