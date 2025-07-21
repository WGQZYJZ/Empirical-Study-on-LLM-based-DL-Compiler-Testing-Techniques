'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.square\ntorch.Tensor.square(_input_tensor)\n'
import torch
_input_tensor = torch.Tensor([[1, 2, 3], [4, 5, 6]])
_output_tensor = _input_tensor.square()
print('Input Tensor: ', _input_tensor)
print('Output Tensor: ', _output_tensor)