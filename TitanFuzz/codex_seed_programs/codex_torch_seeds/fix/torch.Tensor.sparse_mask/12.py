'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sparse_mask\ntorch.Tensor.sparse_mask(_input_tensor, mask)\n'
import torch
import torch
_input_tensor = torch.randn(3, 3, 3, 3)
mask = torch.tensor([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
output_tensor = torch.Tensor.sparse_mask(_input_tensor, mask)
print(output_tensor)