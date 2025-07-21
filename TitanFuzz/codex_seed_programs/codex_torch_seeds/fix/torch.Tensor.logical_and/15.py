'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.logical_and\ntorch.Tensor.logical_and(_input_tensor, other)\n'
import torch
_input_tensor = torch.tensor([[1, 0, 1], [0, 1, 0]])
other = torch.tensor([[0, 1, 0], [1, 0, 1]])
result = torch.Tensor.logical_and(_input_tensor, other)
print(result)