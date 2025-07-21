'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_set_to\ntorch.Tensor.is_set_to(_input_tensor, tensor)\n'
import torch
_input_tensor = torch.randn((1, 2, 3))
torch.Tensor.is_set_to(_input_tensor, torch.randn((1, 2, 3)))