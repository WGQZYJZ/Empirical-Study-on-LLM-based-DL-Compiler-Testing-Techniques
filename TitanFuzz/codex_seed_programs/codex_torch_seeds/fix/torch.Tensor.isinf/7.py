'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.isinf\ntorch.Tensor.isinf(_input_tensor)\n'
import torch
_input_tensor = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]])
_output_tensor = torch.Tensor.isinf(_input_tensor)
print('Input Tensor:')
print(_input_tensor)
print('Output Tensor:')
print(_output_tensor)