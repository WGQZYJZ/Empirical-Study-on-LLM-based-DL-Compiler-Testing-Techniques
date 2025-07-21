'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.tile\ntorch.Tensor.tile(_input_tensor, dims)\n'
import torch
import torch
_input_tensor = torch.randn(2, 3)
print(torch.Tensor.tile(_input_tensor, dims=(2, 2)))