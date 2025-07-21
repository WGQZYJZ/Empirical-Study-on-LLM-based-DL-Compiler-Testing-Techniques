'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_copy_\ntorch.Tensor.index_copy_(_input_tensor, dim, index, tensor)\n'
import torch
input_tensor = torch.randn(2, 3, 5)
index = torch.tensor([0, 2])
source = torch.randn(2, 5)
torch.Tensor.index_copy_(input_tensor, dim=0, index=index, source=source)
print(input_tensor)