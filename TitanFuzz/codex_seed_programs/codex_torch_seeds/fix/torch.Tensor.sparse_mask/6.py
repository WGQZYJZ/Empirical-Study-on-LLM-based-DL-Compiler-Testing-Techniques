'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sparse_mask\ntorch.Tensor.sparse_mask(_input_tensor, mask)\n'
import torch
import torch
input_tensor = torch.rand(2, 3, 4)
mask = torch.tensor([[0, 1, 1], [1, 0, 1]], dtype=torch.uint8)
print(torch.Tensor.sparse_mask(input_tensor, mask))