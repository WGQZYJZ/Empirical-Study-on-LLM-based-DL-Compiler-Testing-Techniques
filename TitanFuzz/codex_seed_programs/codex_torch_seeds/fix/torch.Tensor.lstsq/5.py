'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.lstsq\ntorch.Tensor.lstsq(_input_tensor, A)\n'
import torch
_input_tensor = torch.randn(3, 2)
A = torch.randn(2, 2)
torch.Tensor.lstsq(_input_tensor, A)