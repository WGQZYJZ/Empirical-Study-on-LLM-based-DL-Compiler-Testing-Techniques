'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_copy_\ntorch.Tensor.index_copy_(_input_tensor, dim, index, tensor)\n'
import torch
input_tensor = torch.randn(3, 3)
torch.Tensor.index_copy_(input_tensor, 0, torch.tensor([1, 2]), torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]))
print(input_tensor)