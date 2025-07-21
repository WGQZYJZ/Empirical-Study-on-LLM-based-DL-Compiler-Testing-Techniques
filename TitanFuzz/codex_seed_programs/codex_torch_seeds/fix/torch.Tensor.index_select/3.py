'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_select\ntorch.Tensor.index_select(_input_tensor, dim, index)\n'
import torch
input_tensor = torch.randn(2, 3)
print(input_tensor)
output_tensor = input_tensor.index_select(0, torch.tensor([0, 1]))
print(output_tensor)