'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.exponential_\ntorch.Tensor.exponential_(_input_tensor, lambd=1, *, generator=None)\n'
import torch
_input_tensor = torch.rand(4, 4)
_output_tensor = _input_tensor.exponential_()
print(_output_tensor)