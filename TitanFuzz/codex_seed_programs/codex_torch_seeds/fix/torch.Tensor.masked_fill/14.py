'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.masked_fill\ntorch.Tensor.masked_fill(_input_tensor, mask, value)\n'
import torch
x = torch.randn(2, 3)
mask = torch.tensor([[0, 1, 0], [1, 1, 1]], dtype=torch.uint8)
x.masked_fill(mask, 0)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.masked_select\ntorch.Tensor.masked_select(_input_tensor, mask)\n'
import torch
x = torch.randn(2, 3)
mask = torch.tensor([[0, 1, 0], [1, 1, 1]], dtype=torch.uint8)
x.masked_select(mask)