'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.apply_\ntorch.Tensor.apply_(_input_tensor, callable)\n'
import torch
_input_tensor = torch.randn(4, 4)
torch.Tensor.apply_(_input_tensor, (lambda x: (x * 2)))