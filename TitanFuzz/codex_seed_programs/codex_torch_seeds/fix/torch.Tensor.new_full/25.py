'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.new_full\ntorch.Tensor.new_full(_input_tensor, size, fill_value, dtype=None, device=None, requires_grad=False)\n'
import torch
_input_tensor = torch.randn(3, 5)
print(_input_tensor)
_output_tensor = torch.Tensor.new_full(_input_tensor, 3, fill_value=10)
print(_output_tensor)