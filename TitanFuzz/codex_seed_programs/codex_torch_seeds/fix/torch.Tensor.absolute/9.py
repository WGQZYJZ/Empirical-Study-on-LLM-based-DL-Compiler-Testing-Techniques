'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.absolute\ntorch.Tensor.absolute(_input_tensor)\n'
import torch
_input_tensor = torch.rand(3, 3)
_output_tensor = _input_tensor.absolute()
print(_output_tensor)