'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.new_full\ntorch.Tensor.new_full(_input_tensor, size, fill_value, dtype=None, device=None, requires_grad=False)\n'
import torch
_input_tensor = torch.randn(1, 2, 3)
print(_input_tensor)
_fill_value = 1
_dtype = torch.int32
_device = 'cuda'
_requires_grad = True
_output_tensor = torch.Tensor.new_full(_input_tensor, _fill_value, _dtype, _device, _requires_grad)
print(_output_tensor)