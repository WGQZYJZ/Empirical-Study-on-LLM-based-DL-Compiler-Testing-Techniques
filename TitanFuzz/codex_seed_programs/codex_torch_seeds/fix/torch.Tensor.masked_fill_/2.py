'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.masked_fill_\ntorch.Tensor.masked_fill_(_input_tensor, mask, value\n'
import torch
in_tensor = torch.rand(2, 3)
mask = torch.tensor([[0, 1, 0], [1, 0, 1]], dtype=torch.uint8)
in_tensor.masked_fill_(mask, 0)
print(in_tensor)