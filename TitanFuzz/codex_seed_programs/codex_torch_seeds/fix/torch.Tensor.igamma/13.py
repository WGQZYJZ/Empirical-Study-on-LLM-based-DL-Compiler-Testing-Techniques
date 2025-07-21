'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.igamma\ntorch.Tensor.igamma(_input_tensor, other)\n'
import torch
import torch
input_tensor = torch.randn(1, 3, 4, 5)
other = torch.randn(1, 3, 4, 5)
output_tensor = input_tensor.igamma(other)
print(output_tensor)