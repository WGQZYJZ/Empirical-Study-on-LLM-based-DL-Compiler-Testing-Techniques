'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sparse_mask\ntorch.Tensor.sparse_mask(_input_tensor, mask)\n'
import torch
input_tensor = torch.randn(3, 4)
mask = torch.tensor([0, 1, 0, 1], dtype=torch.bool)
output_tensor = input_tensor.sparse_mask(mask)
print(input_tensor)
print(output_tensor)