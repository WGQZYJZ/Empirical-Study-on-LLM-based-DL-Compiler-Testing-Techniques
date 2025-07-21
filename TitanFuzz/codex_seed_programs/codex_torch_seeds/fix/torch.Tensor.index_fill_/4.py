'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_fill_\ntorch.Tensor.index_fill_(_input_tensor, dim, index, value)\n'
import torch
input_tensor = torch.rand(2, 3)
print(input_tensor)
output_tensor = input_tensor.clone()
output_tensor.index_fill_(0, torch.tensor([0]), 0)
print(output_tensor)