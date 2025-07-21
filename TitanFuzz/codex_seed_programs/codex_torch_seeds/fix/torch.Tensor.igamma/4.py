'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.igamma\ntorch.Tensor.igamma(_input_tensor, other)\n'
import torch
_input_tensor = torch.rand(2, 3)
other = torch.rand(2, 3)
result = _input_tensor.igamma(other)
print(result)