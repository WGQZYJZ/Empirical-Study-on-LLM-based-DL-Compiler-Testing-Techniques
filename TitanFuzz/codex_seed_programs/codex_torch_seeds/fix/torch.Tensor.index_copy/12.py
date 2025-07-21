'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_copy\ntorch.Tensor.index_copy(_input_tensor, dim, index, tensor2)\n'
import torch
input_tensor = torch.randn(4, 4)
index = torch.tensor([0, 2])
source = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8]])
output_tensor = input_tensor.index_copy(dim=0, index=index, source=source)
print(output_tensor)