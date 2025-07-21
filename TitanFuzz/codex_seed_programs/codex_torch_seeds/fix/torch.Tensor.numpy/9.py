'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.numpy\ntorch.Tensor.numpy(_input_tensor)\n'
import torch
_input_tensor = torch.randn(3, 4)
print(_input_tensor)
_output_numpy = _input_tensor.numpy()
print(_output_numpy)
_input_tensor[(0, 0)] = (- 1)
print(_output_numpy)