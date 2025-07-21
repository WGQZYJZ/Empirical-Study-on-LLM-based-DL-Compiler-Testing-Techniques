'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.t\ntorch.Tensor.t(_input_tensor)\n'
import torch
_input_tensor = torch.randint(10, (3, 3), dtype=torch.float32)
print('Input tensor:')
print(_input_tensor)
_transposed_tensor = _input_tensor.t()
print('Transposed tensor:')
print(_transposed_tensor)