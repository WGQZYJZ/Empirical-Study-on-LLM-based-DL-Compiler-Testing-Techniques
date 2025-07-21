'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.dot\ntorch.Tensor.dot(_input_tensor, other)\n'
import torch
_input_tensor = torch.randint(10, (2, 3), dtype=torch.float)
_output_tensor = _input_tensor.dot(_input_tensor)
print(_input_tensor)
print(_output_tensor)