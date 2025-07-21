'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.lstsq\ntorch.Tensor.lstsq(_input_tensor, A)\n'
import torch
_input_tensor = torch.rand(3, 3)
A = torch.rand(3, 3)
torch.Tensor.lstsq(_input_tensor, A)