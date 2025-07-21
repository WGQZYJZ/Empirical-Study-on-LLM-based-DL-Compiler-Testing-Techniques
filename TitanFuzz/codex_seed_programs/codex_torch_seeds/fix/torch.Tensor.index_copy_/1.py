'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_copy_\ntorch.Tensor.index_copy_(_input_tensor, dim, index, tensor)\n'
import torch
data = torch.rand(5, 3)
print(data)
print(data.index_copy_(0, torch.tensor([0, 2]), torch.tensor([[0, 0, 0], [1, 1, 1]])))