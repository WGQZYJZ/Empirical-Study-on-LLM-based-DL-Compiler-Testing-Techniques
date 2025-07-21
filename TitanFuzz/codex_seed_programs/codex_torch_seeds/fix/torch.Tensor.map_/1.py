'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.map_\ntorch.Tensor.map_(_input_tensor, tensor, callable\n'
import torch
_input_tensor = torch.tensor([[1, 2], [3, 4]])
torch.Tensor.map_(_input_tensor, (lambda x: (x + 1)))