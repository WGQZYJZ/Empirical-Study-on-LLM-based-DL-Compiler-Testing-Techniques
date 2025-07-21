'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.igamma_\ntorch.Tensor.igamma_(_input_tensor, other)\n'
import torch
input_tensor = torch.randn(20, 30)
other = torch.randn(20, 30)
output_tensor = input_tensor.igamma_(other)
print(output_tensor)