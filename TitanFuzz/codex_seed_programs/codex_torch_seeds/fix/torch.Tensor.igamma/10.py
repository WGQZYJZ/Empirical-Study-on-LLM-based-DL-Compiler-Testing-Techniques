'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.igamma\ntorch.Tensor.igamma(_input_tensor, other)\n'
import torch
import numpy as np
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
other = torch.tensor([1, 2, 3])
result = torch.Tensor.igamma(input_tensor, other)
print(result)