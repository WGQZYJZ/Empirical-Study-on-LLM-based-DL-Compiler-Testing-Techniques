'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.repeat\ntorch.Tensor.repeat(_input_tensor, *sizes)\n'
import torch
_input_tensor = torch.Tensor([[1, 2, 3], [4, 5, 6]])
_input_tensor = _input_tensor.repeat(2, 2)
print(_input_tensor)