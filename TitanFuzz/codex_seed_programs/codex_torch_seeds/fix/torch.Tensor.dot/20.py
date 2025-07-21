'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.dot\ntorch.Tensor.dot(_input_tensor, other)\n'
import torch
_input_tensor = torch.rand(4, 3)
_input_tensor_2 = torch.rand(3, 5)
_output_tensor = _input_tensor.dot(_input_tensor_2)
print(_output_tensor)