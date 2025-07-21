'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.flatten\ntorch.Tensor.flatten(_input_tensor, start_dim=0, end_dim=-1)\n'
import torch
_input_tensor = torch.randn(1, 2, 3, 4)
_output_tensor = _input_tensor.flatten(start_dim=1, end_dim=3)
print(_output_tensor)
_output_tensor = _input_tensor.flatten(start_dim=1, end_dim=2)
print(_output_tensor)
_output_tensor = _input_tensor.flatten(start_dim=1, end_dim=1)
print(_output_tensor)