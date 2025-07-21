'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.logical_and\ntorch.Tensor.logical_and(_input_tensor, other)\n'
import torch
import torch
_input_tensor = torch.randint(low=0, high=2, size=(4, 4), dtype=torch.float32)
other = torch.randint(low=0, high=2, size=(4, 4), dtype=torch.float32)
torch.Tensor.logical_and(_input_tensor, other)