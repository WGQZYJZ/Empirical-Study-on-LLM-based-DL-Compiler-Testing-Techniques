'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.take\ntorch.Tensor.take(_input_tensor, indices)\n'
import torch
_input_tensor = torch.randint(0, 10, (5, 5))
print('Input tensor:\n', _input_tensor)
indices = torch.tensor([1, 3])
print('Indices:\n', indices)
print('Output tensor:\n', _input_tensor.take(indices))