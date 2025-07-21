'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_fill\ntorch.Tensor.index_fill(_input_tensor, dim, index, value)\n'
import torch
import torch
input_tensor = torch.randn(3, 4)
torch.Tensor.index_fill(input_tensor, 0, torch.tensor([0, 2]), (- 100))
print(input_tensor)