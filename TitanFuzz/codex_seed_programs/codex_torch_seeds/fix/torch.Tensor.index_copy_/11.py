'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_copy_\ntorch.Tensor.index_copy_(_input_tensor, dim, index, tensor)\n'
import torch
input_tensor = torch.randn(2, 3)
print('input_tensor:')
print(input_tensor)
index = torch.tensor([0, 2])
output_tensor = input_tensor.index_copy_(0, index, torch.tensor([[1, 2, 3], [4, 5, 6]]))
print('output_tensor:')
print(output_tensor)