'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_leaf\ntorch.Tensor.is_leaf(_input_tensor, )\n'
import torch
input_tensor = torch.rand(3, 3)
print(torch.Tensor.is_leaf(input_tensor))