'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.igamma\ntorch.Tensor.igamma(_input_tensor, other)\n'
import torch
_input_tensor = torch.randn(4, 4)
other = torch.randn(4, 4)
print(torch.Tensor.igamma(_input_tensor, other))