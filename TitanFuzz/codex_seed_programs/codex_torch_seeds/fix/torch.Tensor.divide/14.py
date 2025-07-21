'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.divide\ntorch.Tensor.divide(_input_tensor, value, *, rounding_mode=None)\n'
import torch
_input_tensor = torch.randint(low=1, high=10, size=(3, 3), dtype=torch.float32)
print('Input Tensor:', _input_tensor)
output_tensor = _input_tensor.divide(2)
print('Output Tensor:', output_tensor)