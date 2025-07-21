'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sparse_mask\ntorch.Tensor.sparse_mask(_input_tensor, mask)\n'
import torch
_input_tensor = torch.randn(2, 3, 4)
mask = torch.randn(2, 3, 4)
output_tensor = _input_tensor.sparse_mask(mask)
print(output_tensor)