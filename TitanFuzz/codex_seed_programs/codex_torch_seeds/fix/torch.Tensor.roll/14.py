'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.roll\ntorch.Tensor.roll(_input_tensor, shifts, dims)\n'
import torch
_input_tensor = torch.randn(2, 3)
_output_tensor = _input_tensor.roll(1, 0)
print(_output_tensor)
_output_tensor = _input_tensor.roll(2, 1)
print(_output_tensor)
_output_tensor = _input_tensor.roll((- 1), 1)
print(_output_tensor)