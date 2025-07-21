'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sparse_mask\ntorch.Tensor.sparse_mask(_input_tensor, mask)\n'
import torch
import torch
_input_tensor = torch.rand(3, 4)
mask = torch.tensor([[1, 1, 0, 0], [0, 0, 0, 1], [1, 0, 1, 0]], dtype=torch.uint8)
output_tensor = torch.Tensor.sparse_mask(_input_tensor, mask)
print(output_tensor)