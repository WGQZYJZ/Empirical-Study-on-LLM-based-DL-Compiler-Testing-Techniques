'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.apply_\ntorch.Tensor.apply_(_input_tensor, callable)\n'
import torch
_input_tensor = torch.rand(2, 3)
torch.Tensor.apply_(_input_tensor, (lambda x: (x + 1)))