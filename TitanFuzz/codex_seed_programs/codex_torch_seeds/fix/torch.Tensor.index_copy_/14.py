'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_copy_\ntorch.Tensor.index_copy_(_input_tensor, dim, index, tensor)\n'
import torch
input_tensor = torch.rand(3, 5)
print(input_tensor)
index_copy_tensor = input_tensor.index_copy_(0, torch.tensor([2]), input_tensor[0, :])
print(index_copy_tensor)
index_copy_tensor = input_tensor.index_copy_(1, torch.tensor([4]), input_tensor[:, 0])
print(index_copy_tensor)