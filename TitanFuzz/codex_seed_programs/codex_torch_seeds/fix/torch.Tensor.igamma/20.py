'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.igamma\ntorch.Tensor.igamma(_input_tensor, other)\n'
import torch
import torch
input_tensor = torch.randn(2, 3, 4, 5)
other = torch.randn(2, 3, 4, 5)
result = input_tensor.igamma(other)
print(result)