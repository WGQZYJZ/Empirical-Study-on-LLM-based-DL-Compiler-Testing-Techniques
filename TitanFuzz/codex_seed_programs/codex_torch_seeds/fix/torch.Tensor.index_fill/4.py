'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_fill\ntorch.Tensor.index_fill(_input_tensor, dim, index, value)\n'
import torch
input_tensor = torch.rand(3, 5)
output_tensor = torch.Tensor.index_fill(input_tensor, 0, torch.tensor([1, 2]), 1)
print(output_tensor)